# Plan: Jira AI Test Case Generator - Streamlit Application

## TL;DR
Build a Python Streamlit application with two pages:
1. **Settings Page**: Configure Jira credentials (URL, email, token) and AI model preferences (Ollama or Groq)
2. **Test Case Generator Page**: ChatGPT-style interface to fetch Jira tickets and generate test cases using local Ollama or Groq API fallback

Uses `.env` file to securely store credentials. Generates test cases following the QA template structure defined in `templates/local_testcasegenerator.md`.

---

## Implementation Phases & Steps

### **Phase 1: Project Setup & Environment**

**Step 1: Create Directory Structure**
- `src/app.py` — Main Streamlit application entry point
- `src/config.py` — Environment variable loader and configuration manager
- `src/pages/settings.py` — Settings page (Streamlit multi-page support)
- `src/pages/generator.py` — Test case generator page
- `src/integrations/jira_connector.py` — Jira REST API integration
- `src/integrations/llm_connector.py` — Ollama and Groq API handlers
- `src/utils/prompt_builder.py` — Construct LLM prompts with Jira context and templates
- `src/utils/test_case_formatter.py` — Format LLM output into structured test cases
- `.env` — Credentials file (git-ignored)
- `requirements.txt` — Python dependencies

**Step 2: Create `.env` File with Credentials**
```
JIRA_URL=https://your-jira-instance.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_TOKEN=your-jira-api-token
GROQ_API_KEY=your-groq-api-key
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

**Step 3: Create requirements.txt**
Dependencies:
- streamlit (UI framework)
- requests (HTTP client for Jira & Groq)
- python-dotenv (Load .env variables)
- ollama (Ollama Python client)

---

### **Phase 2: Core Integration Logic**

**Step 4: Jira Connector** (`src/integrations/jira_connector.py`)
- Load Jira credentials from .env via `config.py`
- Implement `fetch_jira_issue(issue_key)` — Returns title, description, acceptance criteria
- Handle authentication errors gracefully
- Parse Jira response into structured dict

**Step 5: LLM Connector** (`src/integrations/llm_connector.py`)
- Implement `generate_test_cases_ollama(context, template)` — Send request to local Ollama
- Implement `generate_test_cases_groq(context, template)` — Fallback to Groq API
- Auto-detect Ollama availability; fall back to Groq if unavailable
- Return formatted test case string

**Step 6: Prompt Builder** (`src/utils/prompt_builder.py`)
- Load test case template from `templates/local_testcasegenerator.md`
- Build system prompt: "You are a Senior QA Architect. Generate test cases following this structure: [template]"
- Construct user prompt: "Generate test cases for: [Jira issue details]"
- Inject RICEPOT instructions if needed (from `src/FinetunePrompt.md`)

---

### **Phase 3: Frontend Pages**

**Step 7: Settings Page** (`src/pages/settings.py`)
- Streamlit form to input/update:
  - Jira URL, email, token
  - Ollama URL and model name
  - Groq API key
- Save inputs to `.env` file securely
- Validate connectivity: "Test Jira Connection" button → test API call
- Display status: "✅ Connected to Jira" or "❌ Connection Failed"

**Step 8: Test Case Generator Page** (`src/pages/generator.py`)
- ChatGPT-like chat interface using Streamlit `chat_input()` and `chat_message()`
- User input field: "Ask me to create test cases for a Jira issue..."
- On submit:
  - Extract Jira issue key (e.g., ABC-123)
  - Call `jira_connector.fetch_jira_issue(key)`
  - Call `prompt_builder.build_prompt(jira_details, template)`
  - Call `llm_connector.generate_test_cases()` (Ollama first, then Groq if needed)
  - Display result in chat format
  - Add "Download as MD" button

---

### **Phase 4: Main Application & Integration**

**Step 9: Main App** (`src/app.py`)
- Initialize Streamlit multipage app
- Set page configuration (title, layout, sidebar)
- Import both pages (Settings and Generator)
- Add navigation sidebar
- Include error handling and logging

---

## Key Files Used

- `src/FinetunePrompt.md` — RICEPOT prompt structure and QA role definition (reference for LLM system instructions)
- `templates/local_testcasegenerator.md` — Test case template structure with table format (reference for output formatting)
- `.env` — Stores: JIRA_URL, JIRA_EMAIL, JIRA_TOKEN, GROQ_API_KEY, OLLAMA_URL, OLLAMA_MODEL

---

## Verification Checklist

- [ ] Environment setup: `.env` created with all keys
- [ ] `pip install -r requirements.txt` succeeds
- [ ] Settings page: Form renders correctly, Jira connection test succeeds
- [ ] Jira fetch: Enter valid issue key → returns title, description, acceptance criteria
- [ ] LLM integration: Ollama available → generates test cases; Ollama down → Groq fallback works
- [ ] Test Case Generator page: Chat interface accepts input and displays generated test cases
- [ ] End-to-end flow: User enters Jira ID → fetches details → generates test cases → exports as Markdown

---

## Architecture Decisions

- **Ollama as primary LLM**: Assumes local Ollama running on `localhost:11434` with `llama3.2` loaded
- **Groq as fallback**: Only used if Ollama unavailable or explicitly selected by user
- **Credential storage**: `.env` file (git-ignored, never committed)
- **Frontend framework**: Streamlit only (lightweight, no complex UI needed)
- **Export format**: Markdown (initially; can extend to JSON/CSV/PDF later)
- **Platform**: Windows-compatible (all dependencies are cross-platform)
- **Scope**: Single-user, no database, no authentication layer

---

## Status: READY FOR IMPLEMENTATION
