# Jira AI Test Case Generator - Quick Start Guide

## Prerequisites

- Python 3.8 or higher
- Jira account with API token access
- Either:
  - **Ollama** running locally with llama3.2 installed, OR
  - **Groq** API key for cloud-based LLM

## Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure Credentials

Edit the `.env` file with your credentials:

```env
JIRA_URL=https://your-instance.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_TOKEN=your-api-token
GROQ_API_KEY=your-groq-key (optional)
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### Step 3: Start Ollama (if using local LLM)

```bash
ollama serve
# In another terminal:
ollama pull llama3.2
```

### Step 4: Run the Application

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

Or directly:
```bash
streamlit run src/app.py
```

The application will open at `http://localhost:8501`

## Getting Your Credentials

### Jira API Token
1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Create a new API token
3. Copy and paste into `.env` file

### Ollama Setup
1. Download from https://ollama.ai
2. Install and run: `ollama serve`
3. Pull model: `ollama pull llama3.2`
4. Default runs on `http://localhost:11434`

### Groq API Key
1. Sign up at https://console.groq.com
2. Generate API key
3. Copy into `.env` file

## Usage

1. Go to **Settings** tab to configure Jira and LLM
2. Click "Test Connection" to verify credentials
3. Go to **Test Case Generator** tab
4. Enter a Jira issue key (e.g., "ABC-123")
5. AI generates comprehensive test cases
6. Download as Markdown or copy to clipboard

## Troubleshooting

### "Jira connection failed"
- Check JIRA_URL format (should be `https://your-instance.atlassian.net`)
- Verify API token is correct
- Ensure your Jira account has API access enabled

### "Cannot connect to Ollama"
- Make sure Ollama is running: `ollama serve`
- Check OLLAMA_URL in `.env` (default: `http://localhost:11434`)
- Verify the model is installed: `ollama list`

### "Groq connection failed"
- Check GROQ_API_KEY in `.env`
- Ensure your Groq API key is valid
- Check internet connection (Groq requires internet)

### "Slow test case generation"
- For Ollama: Larger models take longer. llama3.2 is optimized for speed
- For Groq: Network latency may vary. Try again or check Groq status

## Project Structure

```
chapter3_localtestcasegenerator/
├── src/
│   ├── app.py                      # Main Streamlit app
│   ├── config.py                   # Configuration manager
│   ├── FinetunePrompt.md          # RICEPOT prompt template
│   ├── Prompt.md                   # Original requirements
│   ├── plan.md                     # Implementation plan
│   ├── integrations/
│   │   ├── jira_connector.py      # Jira API integration
│   │   └── llm_connector.py       # Ollama & Groq integration
│   ├── utils/
│   │   ├── prompt_builder.py      # Prompt construction
│   │   └── test_case_formatter.py # Output formatting
│   └── pages/
│       ├── settings.py             # Settings configuration page
│       └── generator.py            # Test case generator page
├── templates/
│   └── local_testcasegenerator.md # Test case template
├── .env                            # Environment variables (git-ignored)
├── .gitignore                      # Git ignore file
├── requirements.txt                # Python dependencies
├── run.bat                         # Windows startup script
├── run.sh                          # Linux/Mac startup script
└── QUICKSTART.md                   # This file
```

## Features

✨ **AI-Powered Generation**
- Uses Ollama (local) or Groq (cloud) for test case generation
- RICEPOT framework for structured prompts
- Covers positive, negative, edge, and regression scenarios

🔒 **Security**
- Credentials stored locally in `.env` (git-ignored)
- Local Ollama option for privacy
- No sensitive data logged

⚡ **Performance**
- Fast local processing with Ollama
- Automatic fallback to Groq if Ollama unavailable
- ChatGPT-like interface for quick interaction

📥 **Export Options**
- Download as Markdown file
- Copy to clipboard
- Ready to import into test management systems

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify all credentials in Settings tab
3. Check error messages in the Streamlit console
4. Review logs in `.streamlit/logs/`

## License

[Your License Here]

## Changelog

### Version 1.0.0
- Initial release
- Jira integration
- Ollama and Groq support
- Streamlit frontend with Settings and Generator pages
- Markdown export capability
