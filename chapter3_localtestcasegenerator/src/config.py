"""
Configuration Manager
Loads and validates environment variables from .env file
"""

import os
from dotenv import load_dotenv

# Load .env file from parent directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


class Config:
    """Configuration class for Jira and LLM settings"""

    # Jira Configuration
    JIRA_URL = os.getenv("JIRA_URL", "").strip()
    JIRA_EMAIL = os.getenv("JIRA_EMAIL", "").strip()
    JIRA_TOKEN = os.getenv("JIRA_TOKEN", "").strip()

    # Groq Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()

    # Ollama Configuration
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434").strip()
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2").strip()

    @staticmethod
    def validate_jira():
        """Validate Jira configuration"""
        if not Config.JIRA_URL or not Config.JIRA_EMAIL or not Config.JIRA_TOKEN:
            return False, "Missing Jira credentials (URL, Email, or Token)"
        return True, "Jira configuration valid"

    @staticmethod
    def validate_ollama():
        """Validate Ollama configuration"""
        if not Config.OLLAMA_URL or not Config.OLLAMA_MODEL:
            return False, "Missing Ollama configuration"
        return True, "Ollama configuration valid"

    @staticmethod
    def validate_groq():
        """Validate Groq configuration"""
        if not Config.GROQ_API_KEY:
            return False, "Missing Groq API key"
        return True, "Groq configuration valid"

    @staticmethod
    def update_config(key, value):
        """Update .env file with new configuration"""
        env_file = os.path.join(os.path.dirname(__file__), '..', '.env')
        
        # Read current .env content
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                lines = f.readlines()
        else:
            lines = []

        # Update or add the key
        updated = False
        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}\n"
                updated = True
                break

        if not updated:
            lines.append(f"{key}={value}\n")

        # Write back to .env
        with open(env_file, 'w') as f:
            f.writelines(lines)

        # Reload the configuration
        load_dotenv(env_file, override=True)
        setattr(Config, key, value)

    @staticmethod
    def get_all_config():
        """Get all configuration as dict"""
        return {
            "JIRA_URL": Config.JIRA_URL,
            "JIRA_EMAIL": Config.JIRA_EMAIL,
            "JIRA_TOKEN": Config.JIRA_TOKEN,
            "GROQ_API_KEY": Config.GROQ_API_KEY,
            "OLLAMA_URL": Config.OLLAMA_URL,
            "OLLAMA_MODEL": Config.OLLAMA_MODEL,
        }
