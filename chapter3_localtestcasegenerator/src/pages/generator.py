"""
Test Case Generator Page
ChatGPT-like interface for generating test cases from Jira issues
"""

import streamlit as st
import sys
import os
import re

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from integrations.jira_connector import get_jira_connector
from integrations.llm_connector import get_llm_connector
from utils.prompt_builder import get_prompt_builder
from utils.test_case_formatter import get_test_case_formatter


def extract_issue_key(text: str) -> str:
    """Extract Jira issue key from text (e.g., ABC-123)"""
    match = re.search(r'[A-Z]+-\d+', text)
    return match.group(0) if match else ""


def render_generator_page():
    """Render the test case generator page"""
    st.set_page_config(page_title="Test Case Generator", layout="wide")
    
    st.title("🧪 Jira AI Test Case Generator")
    st.markdown("Generate comprehensive QA test cases from your Jira issues")
    st.divider()

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "current_issue" not in st.session_state:
        st.session_state.current_issue = None
    
    if "generated_cases" not in st.session_state:
        st.session_state.generated_cases = None

    # Sidebar configuration
    with st.sidebar:
        st.markdown("### Quick Settings")
        
        # Check Jira connection status
        jira_valid, jira_msg = Config.validate_jira()
        if jira_valid:
            st.success("✅ Jira configured")
        else:
            st.error("❌ Jira not configured")
            st.info("Please configure Jira in Settings tab first")

        # Check LLM availability
        llm = get_llm_connector()
        ollama_available = llm.check_ollama_availability()
        
        if ollama_available:
            st.info("🦙 Using Ollama (Local)")
        else:
            if Config.GROQ_API_KEY:
                st.info("🚀 Ollama unavailable, will use Groq (Fallback)")
            else:
                st.error("❌ No LLM configured")

    # Chat history display
    st.markdown("### Chat History")
    
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    st.divider()

    # Input area
    st.markdown("### Generate Test Cases")
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Ask me to generate test cases for a Jira issue:",
            placeholder="e.g., Create test cases for ABC-123",
            key="test_case_input"
        )

    with col2:
        send_button = st.button("📤 Send", key="send_button", use_container_width=True)

    # Process user input
    if send_button and user_input:
        # Add user message to chat
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Extract issue key
        issue_key = extract_issue_key(user_input)

        if not issue_key:
            error_msg = "❌ I couldn't find a valid Jira issue key (e.g., ABC-123) in your message. Please try again."
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_msg
            })
        else:
            # Validate Jira config
            if not Config.JIRA_URL or not Config.JIRA_EMAIL or not Config.JIRA_TOKEN:
                error_msg = "❌ Jira is not configured. Please go to Settings and configure your Jira credentials."
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
            else:
                # Show loading state
                with st.spinner(f"⏳ Generating test cases for {issue_key}..."):
                    try:
                        # Step 1: Fetch Jira issue
                        status_msg = f"📍 Fetching Jira issue {issue_key}..."
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": status_msg
                        })

                        jira = get_jira_connector()
                        jira_issue = jira.fetch_issue(issue_key)

                        if not jira_issue:
                            error_msg = f"❌ Could not fetch issue {issue_key}. Please check:\n- Issue key is correct\n- Jira credentials are valid\n- Issue is accessible"
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": error_msg
                            })
                        else:
                            st.session_state.current_issue = jira_issue

                            # Step 2: Build prompt
                            prompt_builder = get_prompt_builder()
                            system_prompt, user_prompt = prompt_builder.build_full_prompt(jira_issue)

                            # Step 3: Generate test cases
                            status_msg = f"🤖 Generating test cases using AI..."
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": status_msg
                            })

                            llm = get_llm_connector()
                            test_cases = llm.generate_test_cases(system_prompt, user_prompt)

                            if not test_cases:
                                error_msg = "❌ Failed to generate test cases. Please check:\n- LLM connection\n- API credentials\n- Network connectivity"
                                st.session_state.messages.append({
                                    "role": "assistant",
                                    "content": error_msg
                                })
                            else:
                                # Step 4: Format output
                                formatter = get_test_case_formatter()
                                test_cases = formatter.clean_output(test_cases)
                                test_cases = formatter.format_as_markdown(test_cases)
                                st.session_state.generated_cases = test_cases

                                # Count test cases
                                test_count = formatter.count_test_cases(test_cases)

                                # Success message with test cases
                                success_msg = f"""✅ Successfully generated {test_count} test cases for {issue_key}

**Issue:** {jira_issue.get('summary', 'N/A')}

---

{test_cases}"""

                                st.session_state.messages.append({
                                    "role": "assistant",
                                    "content": success_msg
                                })

                    except Exception as e:
                        error_msg = f"❌ An error occurred: {str(e)}"
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg
                        })

        # Rerun to show updated chat
        st.rerun()

    # Export options
    if st.session_state.generated_cases:
        st.divider()
        st.markdown("### Export Options")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📋 Copy to Clipboard", key="copy_button"):
                st.code(st.session_state.generated_cases, language="markdown")
                st.success("✅ Copied! (Use Ctrl+C in the code block above)")

        with col2:
            # Export as Markdown file
            formatter = get_test_case_formatter()
            issue_key = st.session_state.current_issue.get("key", "TestCases") if st.session_state.current_issue else "TestCases"
            markdown_content = formatter.export_as_markdown(
                st.session_state.generated_cases,
                issue_key
            )

            st.download_button(
                label="⬇️ Download as .md",
                data=markdown_content,
                file_name=f"{issue_key}_test_cases.md",
                mime="text/markdown",
                key="download_button"
            )

        with col3:
            if st.button("🔄 Clear Chat", key="clear_button"):
                st.session_state.messages = []
                st.session_state.current_issue = None
                st.session_state.generated_cases = None
                st.rerun()


if __name__ == "__main__":
    render_generator_page()
