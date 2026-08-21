# Jira AI Test Case Generator

A Python Streamlit application that automatically generates comprehensive QA test cases from Jira issues using AI (Ollama or Groq).

## 🎯 Overview

This application provides a ChatGPT-like interface where QA engineers can:
- Enter a Jira issue key (e.g., ABC-123)
- Automatically fetch issue details, description, and acceptance criteria
- Generate comprehensive test cases using AI (local Ollama or cloud Groq)
- Export test cases as Markdown files
- Store and manage credentials securely

## ✨ Features

- **🤖 AI-Powered Test Case Generation** — Uses RICEPOT framework for structured prompts
- **🦙 Local Ollama Support** — Run AI models locally for privacy and speed
- **🚀 Groq Fallback** — Automatic fallback to Groq API if Ollama unavailable
- **💻 ChatGPT-like Interface** — Familiar interaction model with Streamlit
- **🔒 Secure Credentials** — Environment variables stored in .env (git-ignored)
- **📥 Export Functionality** — Download as Markdown or copy to clipboard
- **⚙️ Easy Configuration** — Web-based settings page for credential management

## 📋 Requirements

- **Python:** 3.8 or higher
- **Jira:** Cloud instance with API token access
- **LLM:** Either Ollama (local) or Groq API key

### System Requirements

- **Minimum RAM:** 8GB (for Ollama locally)
- **Disk Space:** 5GB+ (for Ollama models)
- **Internet:** Optional (Ollama works offline; Groq requires internet)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

Edit `.env` file:

```env
# Jira Configuration
JIRA_URL=https://your-instance.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_TOKEN=your-jira-api-token

# Groq Configuration (Optional - for fallback)
GROQ_API_KEY=your-groq-api-key

# Ollama Configuration (Local LLM)
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### 3. Start Ollama (if using local LLM)

```bash
# Terminal 1: Start Ollama server
ollama serve

# Terminal 2: Pull the model
ollama pull llama3.2
```

### 4. Run Application

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

**Or directly:**
```bash
streamlit run src/app.py
```

The app opens at `http://localhost:8501`

## 📖 Usage

### Home Page
- Overview of features and quick start guide
- Architecture diagram
- Links to external services

### Settings Page
- **Jira Configuration:** Enter Jira URL, email, and API token
- **LLM Configuration:** Set up Ollama and/or Groq
- **Connection Tests:** Verify credentials with test buttons

### Test Case Generator Page
- **ChatGPT-like Interface:** Enter requests to generate test cases
- **Jira Integration:** Automatically fetches issue details
- **AI Generation:** Creates comprehensive test cases
- **Export Options:** Download as Markdown or copy to clipboard

### Example Workflow

1. Configure Jira credentials in Settings
2. Test Jira connection
3. Go to Test Case Generator
4. Enter: "Create test cases for ABC-123"
5. Application:
   - Fetches issue ABC-123 from Jira
   - Extracts summary, description, acceptance criteria
   - Sends to Ollama (or Groq) with test case template
   - AI generates comprehensive test cases
6. Review and download as Markdown

## 🔧 Configuration Details

### Getting Jira Credentials

1. **API Token:**
   - Go to https://id.atlassian.com/manage-profile/security/api-tokens
   - Create new API token
   - Copy token to `.env`

2. **Instance URL:**
   - Format: `https://your-instance.atlassian.net`
   - Example: `https://mycompany.atlassian.net`

### Setting Up Ollama

1. **Download:** https://ollama.ai
2. **Install:** Follow platform-specific instructions
3. **Run:**
   ```bash
   ollama serve
   ```
4. **Pull Model:**
   ```bash
   ollama pull llama3.2
   ```
5. **Verify:** Visit `http://localhost:11434/api/tags`

### Setting Up Groq

1. **Sign up:** https://console.groq.com
2. **Create API key:** In account settings
3. **Add to .env:**
   ```env
   GROQ_API_KEY=gsk_...
   ```

## 📁 Project Structure

```
chapter3_localtestcasegenerator/
│
├── src/
│   ├── app.py                      # Main Streamlit application
│   ├── config.py                   # Configuration & .env loader
│   ├── FinetunePrompt.md          # RICEPOT prompt template
│   ├── Prompt.md                   # Original requirements document
│   ├── plan.md                     # Implementation plan
│   │
│   ├── integrations/
│   │   ├── jira_connector.py      # Jira REST API integration
│   │   └── llm_connector.py       # Ollama & Groq LLM integration
│   │
│   ├── utils/
│   │   ├── prompt_builder.py      # Constructs structured prompts
│   │   └── test_case_formatter.py # Formats and validates output
│   │
│   └── pages/
│       ├── settings.py             # Settings configuration page
│       └── generator.py            # Test case generator page
│
├── templates/
│   └── local_testcasegenerator.md # Test case template format
│
├── .env                            # Environment variables (git-ignored)
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
├── run.bat                         # Windows startup script
├── run.sh                          # Linux/Mac startup script
├── QUICKSTART.md                   # Quick start guide
└── README.md                       # This file
```

## 🔌 API Integration Details

### Jira REST API v3
- **Endpoint:** `{JIRA_URL}/rest/api/3/issue/{issue-key}`
- **Authentication:** Bearer token in Authorization header
- **Fetches:** Summary, description, type, status, acceptance criteria, comments

### Ollama API
- **Base URL:** `http://localhost:11434`
- **Endpoint:** `/api/chat`
- **Model:** llama3.2 (configurable)
- **Method:** JSON POST with messages

### Groq API
- **Base URL:** `https://api.groq.com/openai/v1/chat/completions`
- **Model:** mixtral-8x7b-32768 (Groq's default)
- **Authentication:** Bearer token in Authorization header

## 🛠️ Troubleshooting

### "Cannot connect to Jira"
**Solutions:**
- Verify JIRA_URL format (include https://)
- Check API token is correct and not expired
- Ensure Jira account has API access enabled
- Test manually: `curl -H "Authorization: Bearer $TOKEN" "$JIRA_URL/rest/api/3/myself"`

### "Ollama connection failed"
**Solutions:**
- Start Ollama: `ollama serve`
- Check OLLAMA_URL is correct (default: http://localhost:11434)
- Verify model is installed: `ollama list`
- Pull model if missing: `ollama pull llama3.2`

### "Groq API error"
**Solutions:**
- Verify GROQ_API_KEY is correct
- Check API key hasn't expired
- Ensure API key is active in Groq console
- Check internet connection
- Verify account has remaining API quota

### "Slow test case generation"
**Solutions:**
- For Ollama: Generation speed depends on model size and system RAM
- Switch to faster model: `ollama pull mistral`
- For Groq: Network latency may vary; retry if timeout
- Check system resources (CPU, RAM, Disk)

### "Streamlit not found"
**Solution:**
- Install dependencies: `pip install -r requirements.txt`

### "Application doesn't start"
**Solutions:**
- Check Python version: `python --version` (3.8+)
- Verify .env file exists in project root
- Check error messages in terminal
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## 📊 Architecture

### Data Flow

```
User Input (Jira Issue Key)
    ↓
[Config Loader] → Load credentials from .env
    ↓
[Jira Connector] → Fetch issue details from Jira API
    ↓
[Prompt Builder] → Construct LLM prompt with template
    ↓
[LLM Connector] → Send to Ollama or Groq
    ↓
[Test Case Formatter] → Format and validate output
    ↓
[Streamlit Display] → Show in chat interface
    ↓
[Export Module] → Download or copy to clipboard
```

### Component Overview

| Component | Purpose | Technology |
|-----------|---------|------------|
| **app.py** | Main entry point & routing | Streamlit |
| **config.py** | Credential management | python-dotenv |
| **jira_connector.py** | Jira API communication | requests |
| **llm_connector.py** | LLM communication | requests (Ollama/Groq) |
| **prompt_builder.py** | Prompt construction | Python, file I/O |
| **test_case_formatter.py** | Output formatting | Python string operations |
| **settings.py** | Configuration UI | Streamlit widgets |
| **generator.py** | Main application UI | Streamlit chat widgets |

## 🔐 Security Considerations

- **Credentials Storage:** Keep .env file secure; never commit to version control
- **API Tokens:** Rotate tokens regularly; use strong passwords
- **Local Processing:** Ollama processes data locally; no external calls
- **Groq Fallback:** Use sparingly; minimizes external API calls
- **Firewall:** Ensure Ollama port (11434) is only accessible locally

## 📝 Test Case Template

Generated test cases follow this format:

```markdown
| S.No | Test Case ID | Description | Expected Result | Test Data | Status |
|------|-------------|-------------|-----------------|-----------|--------|
| 1 | TC-001 | [Test description] | [Expected outcome] | [Test data] | ⏳ |
| 2 | TC-002 | ... | ... | ... | ⏳ |
```

Template is loaded from `templates/local_testcasegenerator.md`

## 🎓 Test Case Generation Strategy

The application uses the **RICEPOT Framework**:
- **R**ole: Senior QA Architect
- **I**nstructions: Structured test case generation
- **C**ontext: Jira issue details
- **E**xample: Test case format
- **P**arameters: Test data sets
- **O**utput: Markdown table format
- **T**one: Professional, enterprise-grade

Covers test types:
- ✅ Positive scenarios
- ❌ Negative scenarios
- 🔀 Edge cases
- 🔄 Regression scenarios
- 🚬 Smoke tests
- ✨ Sanity checks

## 📈 Future Enhancements

Potential features for future versions:
- [ ] Test case versioning and history
- [ ] Multiple export formats (JSON, CSV, PDF)
- [ ] Test case templates library
- [ ] User authentication and multi-user support
- [ ] Bulk test case generation from epics
- [ ] Test case prioritization
- [ ] Integration with test management systems
- [ ] Custom prompt templates
- [ ] Test execution tracking

## 📞 Support & Issues

For issues or questions:
1. Check [Troubleshooting](#troubleshooting) section
2. Verify credentials in Settings tab
3. Review error messages in Streamlit console
4. Check `.streamlit/logs/` for detailed logs

## 📄 License

[Add your license here]

## 🙏 Acknowledgments

- RICEPOT framework for prompt structure
- Streamlit for the web framework
- Ollama for local LLM capabilities
- Groq for cloud LLM fallback

## 📚 References

- **Jira API Docs:** https://developer.atlassian.com/cloud/jira/rest/v3
- **Streamlit Docs:** https://docs.streamlit.io
- **Ollama Docs:** https://github.com/ollama/ollama
- **Groq Docs:** https://console.groq.com/docs
- **Python Docs:** https://docs.python.org

---

**Version:** 1.0.0  
**Last Updated:** 2026-08-16  
**Status:** Production Ready ✅
