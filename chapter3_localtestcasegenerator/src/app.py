"""
Jira AI Test Case Generator
Main Streamlit Application Entry Point
"""

import streamlit as st
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from config import Config


def main():
    """Main application entry point"""
    
    # Page configuration
    st.set_page_config(
        page_title="Jira AI Test Case Generator",
        page_icon="🧪",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Apply custom styling
    st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("🧪 Test Case Generator")
    st.sidebar.divider()

    # Navigation links (these are placeholders for multipage routing)
    nav_option = st.sidebar.radio(
        "Navigation",
        ["🏠 Home", "🤖 Test Case Generator", "⚙️ Settings"],
        label_visibility="collapsed"
    )

    # Configuration status in sidebar
    st.sidebar.divider()
    st.sidebar.markdown("### Configuration Status")

    # Check Jira
    jira_valid, _ = Config.validate_jira()
    jira_status = "✅ Configured" if jira_valid else "❌ Not Set"
    st.sidebar.markdown(f"**Jira:** {jira_status}")

    # Check LLM
    from integrations.llm_connector import get_llm_connector
    llm = get_llm_connector()
    ollama_available = llm.check_ollama_availability()
    groq_available = bool(Config.GROQ_API_KEY)

    if ollama_available:
        st.sidebar.markdown("**LLM:** ✅ Ollama Available")
    elif groq_available:
        st.sidebar.markdown("**LLM:** ✅ Groq Configured")
    else:
        st.sidebar.markdown("**LLM:** ❌ Not Set")

    # Route to appropriate page
    if nav_option == "🏠 Home":
        render_home()
    elif nav_option == "🤖 Test Case Generator":
        render_generator()
    elif nav_option == "⚙️ Settings":
        render_settings()


def render_home():
    """Render home page"""
    st.title("🧪 Jira AI Test Case Generator")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## Welcome!
        
        This application helps you generate comprehensive QA test cases directly from your Jira issues using AI.
        
        ### Quick Start
        
        1. **Configure Settings** ⚙️
           - Set up your Jira credentials (URL, email, API token)
           - Configure AI model preferences (Ollama or Groq)
        
        2. **Generate Test Cases** 🤖
           - Go to the "Test Case Generator" page
           - Enter a Jira issue key (e.g., ABC-123)
           - AI generates comprehensive test cases automatically
        
        3. **Export Results** 📥
           - Download as Markdown file
           - Copy to clipboard
           - Use in your test management system
        
        ### Features
        
        ✨ **Intelligent Generation**
        - Uses advanced AI models (Ollama or Groq)
        - Follows QA best practices (RICEPOT framework)
        - Covers positive, negative, edge, and regression scenarios
        
        🔒 **Privacy & Security**
        - Primary LLM runs locally (Ollama)
        - Credentials stored securely in .env
        - No data sent to external services (unless using Groq fallback)
        
        ⚡ **Fast & Efficient**
        - ChatGPT-like interface
        - Real-time test case generation
        - One-click download
        
        ### Getting Started
        
        **Step 1:** Click "Settings" in the sidebar and configure your Jira connection
        
        **Step 2:** Enter your Jira API token and test the connection
        
        **Step 3:** Go to "Test Case Generator" and enter a Jira issue key
        
        **Step 4:** Download or copy your generated test cases
        """)

    with col2:
        st.info("""
        ### 📚 Learn More
        
        **Jira Integration**
        - Generate API token: https://id.atlassian.com/manage-profile/security/api-tokens
        
        **Ollama Setup**
        - Install: https://ollama.ai
        - Download llama3.2: Run `ollama pull llama3.2`
        
        **Groq Setup**
        - Get API key: https://console.groq.com
        - Free tier available for testing
        
        **RICEPOT Framework**
        - Role, Instructions, Context, Example, Parameters, Output, Tone
        """)

    st.divider()

    # Feature highlights
    st.markdown("## How It Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        ### 1️⃣ Enter Issue
        
        Provide a Jira issue key like ABC-123
        """)

    with col2:
        st.markdown("""
        ### 2️⃣ Fetch Details
        
        Automatically retrieve summary, description, and acceptance criteria
        """)

    with col3:
        st.markdown("""
        ### 3️⃣ Generate Cases
        
        AI generates comprehensive test cases using RICEPOT framework
        """)

    with col4:
        st.markdown("""
        ### 4️⃣ Export Results
        
        Download as Markdown or copy to your testing tools
        """)

    st.divider()

    # Architecture overview
    with st.expander("🏗️ Architecture Overview"):
        st.markdown("""
        ```
        User Input
           ↓
        [Streamlit Frontend]
           ↓
        [Config Manager] → reads .env credentials
           ↓
        [Jira Connector] → fetches issue details
           ↓
        [Prompt Builder] → constructs LLM prompt with template
           ↓
        [LLM Connector] → sends to Ollama or Groq
           ↓
        [Test Case Formatter] → formats and validates output
           ↓
        [Streamlit Export] → download or display
        ```
        
        **Technology Stack:**
        - Frontend: Streamlit
        - Backend: Python
        - Primary LLM: Ollama (local)
        - Fallback LLM: Groq API (cloud)
        - APIs: Jira REST API v3
        """)


def render_generator():
    """Render the test case generator page"""
    from pages.generator import render_generator_page
    render_generator_page()


def render_settings():
    """Render the settings page"""
    from pages.settings import render_settings_page
    render_settings_page()


if __name__ == "__main__":
    main()
