"""
Prompt Builder
Constructs LLM prompts with Jira context and test case templates
"""

import os
from typing import Dict, Optional


class PromptBuilder:
    """Builds structured prompts for test case generation"""

    def __init__(self):
        """Initialize prompt builder with templates"""
        self.ricepot_prompt = self._load_ricepot_prompt()
        self.test_case_template = self._load_test_case_template()

    def _load_ricepot_prompt(self) -> str:
        """Load RICEPOT prompt from FinetunePrompt.md"""
        try:
            ricepot_path = os.path.join(
                os.path.dirname(__file__),
                '..',
                'FinetunePrompt.md'
            )
            if os.path.exists(ricepot_path):
                with open(ricepot_path, 'r') as f:
                    return f.read()
        except Exception as e:
            print(f"Error loading RICEPOT prompt: {str(e)}")
        
        return self._default_ricepot_prompt()

    def _load_test_case_template(self) -> str:
        """Load test case template from templates directory"""
        try:
            template_path = os.path.join(
                os.path.dirname(__file__),
                '..',
                '..',
                'templates',
                'local_testcasegenerator.md'
            )
            if os.path.exists(template_path):
                with open(template_path, 'r') as f:
                    return f.read()
        except Exception as e:
            print(f"Error loading test case template: {str(e)}")
        
        return self._default_test_case_template()

    def _default_ricepot_prompt(self) -> str:
        """Default RICEPOT prompt if file not found"""
        return """Act as a Senior QA Architect with expertise in:
- Test case design and execution
- Jira API integration
- QA automation frameworks
- Enterprise testing best practices

Your goal is to generate comprehensive QA test cases based on Jira requirements."""

    def _default_test_case_template(self) -> str:
        """Default test case template if file not found"""
        return """| S.No | Test Case ID | Description | Expected Result | Test Data | Status |
|------|-------------|-------------|-----------------|-----------|--------|"""

    def build_system_prompt(self, use_ricepot: bool = True) -> str:
        """
        Build system prompt for LLM
        
        Args:
            use_ricepot: Whether to use RICEPOT structure
            
        Returns:
            System prompt string
        """
        if use_ricepot:
            system_prompt = f"""{self.ricepot_prompt}

## Test Case Template Format

Use this exact format for all test cases:

{self.test_case_template}

## Instructions
1. Generate comprehensive test cases covering positive, negative, edge, and regression scenarios
2. Follow the template format strictly
3. Each test case should be independent and executable
4. Use clear, descriptive language
5. Include specific test data where applicable
6. Ensure all acceptance criteria from the requirement are covered"""
        else:
            system_prompt = f"""You are a Senior QA Architect. Generate professional QA test cases.

Use this template format:
{self.test_case_template}

Generate at least 15-20 test cases covering:
- Positive scenarios
- Negative scenarios
- Edge cases
- Regression scenarios"""

        return system_prompt

    def build_user_prompt(self, jira_issue: Dict) -> str:
        """
        Build user prompt with Jira context
        
        Args:
            jira_issue: Parsed Jira issue dictionary
            
        Returns:
            User prompt string
        """
        issue_key = jira_issue.get('key', 'UNKNOWN')
        summary = jira_issue.get('summary', '')
        description = jira_issue.get('description', '')
        acceptance_criteria = jira_issue.get('acceptance_criteria', '')
        issue_type = jira_issue.get('type', '')
        status = jira_issue.get('status', '')

        user_prompt = f"""Please generate comprehensive QA test cases for the following Jira issue:

**Issue Key:** {issue_key}
**Type:** {issue_type}
**Status:** {status}

**Summary:**
{summary}

**Description:**
{description}

**Acceptance Criteria:**
{acceptance_criteria}

Generate test cases that:
1. Cover all acceptance criteria
2. Include positive and negative scenarios
3. Test edge cases and boundary conditions
4. Verify error handling and validation
5. Check regression scenarios

Provide the test cases in the specified template format."""

        return user_prompt

    def build_full_prompt(self, jira_issue: Dict, use_ricepot: bool = True) -> tuple[str, str]:
        """
        Build complete system and user prompts
        
        Args:
            jira_issue: Parsed Jira issue dictionary
            use_ricepot: Whether to use RICEPOT structure
            
        Returns:
            Tuple of (system_prompt, user_prompt)
        """
        system_prompt = self.build_system_prompt(use_ricepot)
        user_prompt = self.build_user_prompt(jira_issue)
        return system_prompt, user_prompt


def get_prompt_builder() -> PromptBuilder:
    """Factory function to get prompt builder instance"""
    return PromptBuilder()
