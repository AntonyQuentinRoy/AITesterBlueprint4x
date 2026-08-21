@echo off
REM Start the Jira AI Test Case Generator
REM Make sure you have installed dependencies: pip install -r requirements.txt

cd /d "%~dp0"

echo.
echo ========================================
echo Jira AI Test Case Generator
echo ========================================
echo.
echo Starting application...
echo.
echo ⚠️  Make sure Ollama is running (or Groq API key is configured)
echo 📝 Open your browser to http://localhost:8501
echo.

streamlit run src/app.py

pause
