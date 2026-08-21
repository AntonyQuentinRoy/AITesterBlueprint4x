"""
LLM Connector
Handles connections to Ollama (primary) and Groq (fallback)
"""

import requests
from typing import Optional
from config import Config


class LLMConnector:
    """Manages LLM connections with Ollama as primary and Groq as fallback"""

    def __init__(self):
        """Initialize LLM connector"""
        self.ollama_url = Config.OLLAMA_URL.rstrip('/')
        self.ollama_model = Config.OLLAMA_MODEL
        self.groq_api_key = Config.GROQ_API_KEY
        self.preferred_model = "ollama"  # Default to ollama

    def check_ollama_availability(self) -> bool:
        """Check if Ollama is running and accessible"""
        try:
            response = requests.get(
                f"{self.ollama_url}/api/tags",
                timeout=3
            )
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def generate_test_cases(self, system_prompt: str, user_prompt: str, use_groq: bool = False) -> Optional[str]:
        """
        Generate test cases using LLM
        
        Args:
            system_prompt: System prompt with instructions and context
            user_prompt: User's request
            use_groq: Force use of Groq instead of trying Ollama first
            
        Returns:
            Generated test cases or None if error
        """
        if use_groq:
            return self._generate_with_groq(system_prompt, user_prompt)

        if self.check_ollama_availability():
            ollama_result = self._generate_with_ollama(system_prompt, user_prompt)
            if ollama_result:
                return ollama_result
            print("Ollama generation failed; trying Groq fallback.")

        if self.groq_api_key:
            return self._generate_with_groq(system_prompt, user_prompt)

        print("No usable LLM configured. Start Ollama with the configured model or set GROQ_API_KEY.")
        return None

    def _generate_with_ollama(self, system_prompt: str, user_prompt: str) -> Optional[str]:
        """
        Generate using Ollama (local LLM)
        
        Args:
            system_prompt: System instructions
            user_prompt: User request
            
        Returns:
            Generated response or None if error
        """
        try:
            payload = {
                "model": self.ollama_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False,
                "temperature": 0.7
            }

            response = requests.post(
                f"{self.ollama_url}/api/chat",
                json=payload,
                timeout=60
            )

            if response.status_code == 200:
                data = response.json()
                return (data.get('message') or {}).get('content', '')
            else:
                print(f"Ollama error: {response.status_code} - {response.text}")
                return None

        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Ollama connection error: {str(e)}")
            return None

    def _generate_with_groq(self, system_prompt: str, user_prompt: str) -> Optional[str]:
        """
        Generate using Groq API (fallback)
        
        Args:
            system_prompt: System instructions
            user_prompt: User request
            
        Returns:
            Generated response or None if error
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.groq_api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "openai/gpt-oss-20b",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 2000
            }

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                json=payload,
                headers=headers,
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                choices = data.get('choices') or []
                if not choices or not isinstance(choices[0], dict):
                    return ''
                return (choices[0].get('message') or {}).get('content', '')
            else:
                print(f"Groq error: {response.status_code} - {response.text[:500]}")
                return None

        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Groq connection error: {str(e)}")
            return None

    def switch_model(self, model_type: str) -> bool:
        """
        Switch preferred model
        
        Args:
            model_type: 'ollama' or 'groq'
            
        Returns:
            True if valid model, False otherwise
        """
        if model_type in ["ollama", "groq"]:
            self.preferred_model = model_type
            return True
        return False


def get_llm_connector() -> LLMConnector:
    """Factory function to get LLM connector instance"""
    return LLMConnector()
