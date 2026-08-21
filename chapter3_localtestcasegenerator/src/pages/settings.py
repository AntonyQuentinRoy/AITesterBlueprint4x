"""
Settings Page
Configure Jira and LLM settings
"""

import streamlit as st
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from integrations.jira_connector import get_jira_connector
from integrations.llm_connector import get_llm_connector


def render_settings_page():
    """Render the settings configuration page"""
    st.set_page_config(page_title="Settings", layout="wide")
    
    st.title("⚙️ Settings")
    st.markdown("Configure your Jira and LLM connections")
    st.divider()

    # Create tabs for different configuration sections
    jira_tab, llm_tab, about_tab = st.tabs(["Jira Configuration", "LLM Configuration", "About"])

    # ===== JIRA CONFIGURATION TAB =====
    with jira_tab:
        st.subheader("Jira Connection Settings")
        st.markdown("Configure your Jira instance credentials")

        col1, col2 = st.columns(2)

        with col1:
            jira_url = st.text_input(
                "Jira URL",
                value=Config.JIRA_URL,
                placeholder="https://your-instance.atlassian.net",
                help="Your Jira cloud instance URL"
            )

        with col2:
            jira_email = st.text_input(
                "Jira Email",
                value=Config.JIRA_EMAIL,
                placeholder="your-email@example.com",
                help="Your Jira account email"
            )

        jira_token = st.text_input(
            "Jira API Token",
            value=Config.JIRA_TOKEN,
            type="password",
            placeholder="Enter your API token",
            help="Generate from: https://id.atlassian.com/manage-profile/security/api-tokens"
        )

        # Test Jira Connection Button
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("🔗 Test Connection", key="test_jira"):
                # Update config temporarily
                Config.JIRA_URL = jira_url
                Config.JIRA_EMAIL = jira_email
                Config.JIRA_TOKEN = jira_token

                jira = get_jira_connector()
                success, message = jira.test_connection()

                if success:
                    st.success(message)
                else:
                    st.error(message)

        # Save Jira Settings
        with col2:
            if st.button("💾 Save Settings", key="save_jira"):
                try:
                    Config.update_config("JIRA_URL", jira_url)
                    Config.update_config("JIRA_EMAIL", jira_email)
                    Config.update_config("JIRA_TOKEN", jira_token)
                    st.success("✅ Jira settings saved successfully!")
                except Exception as e:
                    st.error(f"❌ Error saving settings: {str(e)}")

        st.divider()

    # ===== LLM CONFIGURATION TAB =====
    with llm_tab:
        st.subheader("LLM Configuration")
        st.markdown("Configure your AI model preferences")

        # Ollama Configuration
        st.markdown("### 🦙 Ollama (Primary Local LLM)")
        st.info("Ollama runs locally on your machine for faster, private processing")

        col1, col2 = st.columns(2)

        with col1:
            ollama_url = st.text_input(
                "Ollama URL",
                value=Config.OLLAMA_URL,
                placeholder="http://localhost:11434",
                help="URL where Ollama is running"
            )

        with col2:
            ollama_model = st.text_input(
                "Ollama Model",
                value=Config.OLLAMA_MODEL,
                placeholder="llama3.2",
                help="Model name installed in Ollama (e.g., llama3.2, mistral)"
            )

        # Test Ollama Connection
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("🔗 Test Ollama", key="test_ollama"):
                Config.OLLAMA_URL = ollama_url
                Config.OLLAMA_MODEL = ollama_model

                llm = get_llm_connector()
                if llm.check_ollama_availability():
                    st.success("✅ Successfully connected to Ollama")
                else:
                    st.error("❌ Cannot connect to Ollama. Is it running?")

        with col2:
            if st.button("💾 Save Ollama", key="save_ollama"):
                try:
                    Config.update_config("OLLAMA_URL", ollama_url)
                    Config.update_config("OLLAMA_MODEL", ollama_model)
                    st.success("✅ Ollama settings saved!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

        st.divider()

        # Groq Configuration
        st.markdown("### 🚀 Groq API (Fallback Cloud LLM)")
        st.info("Groq is used as fallback if Ollama is unavailable")

        groq_api_key = st.text_input(
            "Groq API Key",
            value=Config.GROQ_API_KEY,
            type="password",
            placeholder="Enter your Groq API key",
            help="Get from: https://console.groq.com"
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.button("🔗 Test Groq", key="test_groq"):
                if groq_api_key:
                    Config.GROQ_API_KEY = groq_api_key
                    llm = get_llm_connector()
                    # Try a simple test call
                    result = llm._generate_with_groq(
                        "You are a helpful assistant.",
                        "Say 'Groq connection successful' if you can read this."
                    )
                    if result:
                        st.success("✅ Successfully connected to Groq")
                    else:
                        st.error("❌ Error connecting to Groq")
                else:
                    st.warning("⚠️ Please enter a Groq API key first")

        with col2:
            if st.button("💾 Save Groq", key="save_groq"):
                try:
                    Config.update_config("GROQ_API_KEY", groq_api_key)
                    st.success("✅ Groq settings saved!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

        st.divider()

        # Model Selection
        st.markdown("### Model Preference")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Ollama Advantages:**
            - 🔒 Private & secure (runs locally)
            - ⚡ Fast responses
            - 💰 Free (no API costs)
            - 📵 Works offline
            """)
        
        with col2:
            st.markdown("""
            **Groq Advantages:**
            - 🌐 Requires internet
            - 🎯 More powerful models
            - 📊 Better for complex tasks
            - 🔄 Automatic fallback
            """)

    # ===== ABOUT TAB =====
    with about_tab:
        st.markdown("""
        ## About This Application
        
        ### Jira AI Test Case Generator
        
        A Streamlit application that generates comprehensive QA test cases from Jira requirements using AI.
        
        **Features:**
        - 🎯 ChatGPT-like interface for test case generation
        - 📋 Automatic Jira ticket retrieval
        - 🤖 AI-powered test case generation using Ollama or Groq
        - 📥 Download generated test cases as Markdown
        - ⚙️ Easy configuration and credential management
        
        **Technology Stack:**
        - **Frontend:** Streamlit
        - **Primary LLM:** Ollama (local)
        - **Fallback LLM:** Groq API (cloud)
        - **Backend:** Python
        
        **How it works:**
        1. Configure Jira and LLM settings here
        2. Go to "Test Case Generator" page
        3. Enter a Jira issue key (e.g., ABC-123)
        4. AI generates comprehensive test cases
        5. Download or copy the results
        
        **Version:** 1.0.0
        """)


if __name__ == "__main__":
    render_settings_page()
