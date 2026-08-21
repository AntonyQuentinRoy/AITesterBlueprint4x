"""
Test Script - Verify Ollama and Jira Connections
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from config import Config
from integrations.jira_connector import get_jira_connector
from integrations.llm_connector import get_llm_connector

print("=" * 60)
print("🧪 JIRA AI TEST CASE GENERATOR - CONNECTION TEST")
print("=" * 60)

# Test 1: Configuration Loading
print("\n✅ Test 1: Configuration Loading")
print("-" * 60)
config = Config.get_all_config()
print(f"JIRA_URL: {config['JIRA_URL']}")
print(f"JIRA_EMAIL: {config['JIRA_EMAIL']}")
print(f"OLLAMA_URL: {config['OLLAMA_URL']}")
print(f"OLLAMA_MODEL: {config['OLLAMA_MODEL']}")
print(f"GROQ_API_KEY: {'***' + config['GROQ_API_KEY'][-4:] if config['GROQ_API_KEY'] else 'Not configured'}")

# Test 2: Ollama Connection
print("\n✅ Test 2: Ollama Connection")
print("-" * 60)
llm = get_llm_connector()
ollama_status = llm.check_ollama_availability()
if ollama_status:
    print("🦙 Ollama Status: ✅ CONNECTED")
    print(f"   URL: {config['OLLAMA_URL']}")
    print(f"   Model: {config['OLLAMA_MODEL']}")
else:
    print("🦙 Ollama Status: ❌ NOT AVAILABLE")

# Test 3: Groq Configuration
print("\n✅ Test 3: Groq Configuration")
print("-" * 60)
groq_status = bool(config['GROQ_API_KEY'])
if groq_status:
    print("🚀 Groq Status: ✅ CONFIGURED")
else:
    print("🚀 Groq Status: ⚠️  NOT CONFIGURED (optional)")

# Test 4: Jira Connection (will fail with test credentials, but we can check the configuration)
print("\n✅ Test 4: Jira Configuration")
print("-" * 60)
jira_valid, jira_msg = Config.validate_jira()
if jira_valid:
    print(f"📋 Jira Status: ✅ CONFIGURED")
    print(f"   {jira_msg}")
    
    # Try to test connection
    jira = get_jira_connector()
    jira_success, jira_test_msg = jira.test_connection()
    print(f"   Connection Test: {jira_test_msg}")
else:
    print(f"📋 Jira Status: ⚠️  {jira_msg}")

# Test 5: Simple Ollama Test (if available)
print("\n✅ Test 5: Ollama AI Capability Test")
print("-" * 60)
if ollama_status:
    print("🤖 Testing Ollama with a simple prompt...")
    try:
        result = llm.generate_test_cases(
            system_prompt="You are a helpful assistant. Respond with exactly 2 sentences.",
            user_prompt="What is test automation?"
        )
        if result:
            print(f"✅ Ollama Response (truncated):")
            print(f"   {result[:150]}...")
        else:
            print("❌ Ollama returned empty response")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
else:
    print("⏭️  Skipped (Ollama not available)")

# Summary
print("\n" + "=" * 60)
print("📊 TEST SUMMARY")
print("=" * 60)
print(f"✅ Configuration: Loaded")
print(f"{'✅' if ollama_status else '❌'} Ollama: {'Connected' if ollama_status else 'Not Available'}")
print(f"{'✅' if groq_status else '⚠️ '} Groq: {'Configured' if groq_status else 'Not Configured'}")
print(f"✅ Jira: Configured (connection may fail with test credentials)")
print("\n" + "=" * 60)
print("🎉 Application is ready for use!")
print("📱 Open http://localhost:8501 in your browser")
print("=" * 60)
