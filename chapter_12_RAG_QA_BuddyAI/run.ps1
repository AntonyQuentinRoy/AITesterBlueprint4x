# QABuddy, locally, in one command (Windows / PowerShell 5.1+).
#
#   .\run.ps1            start Qdrant + Ollama if needed, ingest if the index is empty, serve, open the browser
#   .\run.ps1 ingest     index changed files      (.\run.ps1 ingest -Full rebuilds everything)
#   .\run.ps1 eval       retrieval hit-rate + MRR on eval/golden.yaml, with ablations
#   .\run.ps1 test       regression tests (no services needed)
#   .\run.ps1 ask "Why did build #142 fail?" [-Mode rca]
#   .\run.ps1 demo       re-record the hosted demo (ui/public/demo + api/_prompt.js)
param(
    [string]$Command = "up",
    [string]$Question = "",
    [string]$Mode = "ask",
    [switch]$Full
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Get-EnvValue([string]$Key, [string]$Default) {
    if (Test-Path ".env") {
        $line = Get-Content ".env" | Where-Object { $_ -match "^$Key=" } | Select-Object -First 1
        if ($line) { return ($line -split "=", 2)[1].Trim().Trim('"') }
    }
    return $Default
}

$Port = Get-EnvValue "PORT" "8300"
$EmbedModel = Get-EnvValue "EMBED_MODEL" "qwen3-embedding:0.6b"
$Py = ".venv\Scripts\python.exe"

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env from .env.example. Add GROQ_API_KEY, then re-run."
    exit 1
}

function Start-Qdrant {
    try { Invoke-WebRequest -Uri "http://localhost:6333/" -UseBasicParsing -TimeoutSec 2 | Out-Null; return } catch {}
    $exe = ".bin\qdrant.exe"
    if (-not (Test-Path $exe)) {
        Write-Host "Downloading Qdrant v1.19.1 (windows-msvc)..."
        New-Item -ItemType Directory -Force -Path ".bin" | Out-Null
        $zip = ".bin\qdrant.zip"
        Invoke-WebRequest -Uri "https://github.com/qdrant/qdrant/releases/download/v1.19.1/qdrant-x86_64-pc-windows-msvc.zip" -OutFile $zip
        Expand-Archive -Path $zip -DestinationPath ".bin" -Force
        Remove-Item $zip
    }
    New-Item -ItemType Directory -Force -Path ".qdrant" | Out-Null
    $env:QDRANT__STORAGE__STORAGE_PATH = ".qdrant/storage"
    $env:QDRANT__STORAGE__SNAPSHOTS_PATH = ".qdrant/snapshots"
    $env:QDRANT__TELEMETRY_DISABLED = "true"
    Start-Process -FilePath $exe -WorkingDirectory $PSScriptRoot -RedirectStandardOutput ".qdrant\qdrant.out.log" -RedirectStandardError ".qdrant\qdrant.err.log" -WindowStyle Hidden
    foreach ($i in 1..40) {
        Start-Sleep -Milliseconds 500
        try { Invoke-WebRequest -Uri "http://localhost:6333/" -UseBasicParsing -TimeoutSec 2 | Out-Null; return } catch {}
    }
    throw "Qdrant did not start; see .qdrant\qdrant.err.log"
}

function Start-Ollama {
    if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) { throw "Install Ollama from https://ollama.com, then re-run." }
    try { Invoke-RestMethod -Uri "http://localhost:11434/api/version" -TimeoutSec 2 | Out-Null }
    catch { Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden; Start-Sleep -Seconds 3 }
    $models = ollama list | Out-String
    if ($models -notmatch [regex]::Escape($EmbedModel)) { ollama pull $EmbedModel }
}

function Ensure-PythonEnv {
    if (Test-Path $Py) { return }
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        uv venv --python 3.13 .venv
        uv pip install --python $Py -r requirements.txt pytest
    } else {
        python -m venv .venv
        & $Py -m pip install -q -r requirements.txt pytest
    }
}

function Fetch-Repos {
    # the two framework repos are plain clones (this checkout has no .gitmodules)
    $sel = "data\07_Source_Codes\ATB13xSeleniumAdvanceFramework"
    $pw  = "data\07_Source_Codes\AdvancePlaywrightFramework1x"
    if ((Test-Path "$sel\.git") -and (Test-Path "$pw\.git")) { return }
    Write-Host "Fetching the framework repos..."
    if (-not (Test-Path "$sel\.git")) { git clone --depth 1 https://github.com/PramodDutta/ATB13xSeleniumAdvanceFramework.git $sel }
    if (-not (Test-Path "$pw\.git"))  { git clone --depth 1 https://github.com/PramodDutta/Advance-Playwright-Framework.git $pw }
}

function Build-Ui {
    if (Test-Path "ui\dist\index.html") { return }
    Push-Location ui
    try { npm install --include=dev --silent; npm run build } finally { Pop-Location }
}

switch ($Command) {
    "test"   { Ensure-PythonEnv; & $Py -m pytest -q tests; exit $LASTEXITCODE }
    "ingest" {
        Fetch-Repos; Start-Qdrant; Start-Ollama; Ensure-PythonEnv
        $args2 = @("-m", "qabuddy", "ingest"); if ($Full) { $args2 += "--full" }
        & $Py @args2; exit $LASTEXITCODE
    }
    "eval"   { Start-Qdrant; Start-Ollama; Ensure-PythonEnv; & $Py -m qabuddy eval; exit $LASTEXITCODE }
    "ask"    { Start-Qdrant; Start-Ollama; Ensure-PythonEnv; & $Py -m qabuddy ask $Question --mode $Mode; exit $LASTEXITCODE }
    "demo"   {
        Start-Qdrant; Start-Ollama; Ensure-PythonEnv
        & $Py -m qabuddy export-demo
        Push-Location ui
        try { npm install --include=dev --silent; npm run build:demo } finally { Pop-Location }
        Write-Host "Demo build -> ui/dist-demo (preview: python -m http.server 5310 -d ui/dist-demo). Deploy: vercel --prod"
        exit 0
    }
    default {
        Fetch-Repos; Start-Qdrant; Start-Ollama; Ensure-PythonEnv; Build-Ui
        $points = 0
        try {
            $json = Invoke-RestMethod -Uri "http://localhost:6333/collections/qabuddy" -TimeoutSec 5
            $points = $json.result.points_count
        } catch {}
        if ($points -eq 0) {
            Write-Host "Index is empty: ingesting (first run embeds everything, a few minutes)..."
            & $Py -m qabuddy ingest
        }
        Write-Host "QABuddy -> http://localhost:$Port"
        Start-Process "http://localhost:$Port"
        & $Py -m qabuddy serve
    }
}
