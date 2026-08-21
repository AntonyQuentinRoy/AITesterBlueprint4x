"""
Jira Connector
Handles Jira REST API integration for fetching issue details
"""

import requests
from typing import Dict, Optional
from config import Config


class JiraConnector:
    """Connects to Jira and retrieves issue information"""

    def __init__(self):
        """Initialize Jira connector with configuration"""
        self.base_url = Config.JIRA_URL.rstrip('/')
        self.email = Config.JIRA_EMAIL
        self.token = Config.JIRA_TOKEN
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def test_connection(self) -> tuple[bool, str]:
        """Test Jira connection"""
        try:
            response = requests.get(
                f"{self.base_url}/rest/api/3/myself",
                headers=self.headers,
                auth=(self.email, self.token),
                timeout=5
            )
            if response.status_code == 200:
                return True, "✅ Successfully connected to Jira"
            else:
                return False, f"❌ Jira connection failed: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            return False, f"❌ Connection error: {str(e)}"

    def fetch_issue(self, issue_key: str) -> Optional[Dict]:
        """
        Fetch Jira issue details by issue key
        
        Args:
            issue_key: Jira issue key (e.g., ABC-123)
            
        Returns:
            Dictionary with issue details or None if error
        """
        if not issue_key:
            return None

        try:
            response = requests.get(
                f"{self.base_url}/rest/api/3/issue/{issue_key}",
                headers=self.headers,
                auth=(self.email, self.token),
                timeout=10
            )

            if response.status_code == 200:
                issue_data = response.json()
                return self._parse_issue(issue_data)
            else:
                print(f"Error fetching issue: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Connection error: {str(e)}")
            return None

    def _parse_issue(self, issue_data: Dict) -> Dict:
        """
        Parse Jira issue response into structured format
        
        Args:
            issue_data: Raw issue data from Jira API
            
        Returns:
            Parsed issue dictionary
        """
        fields = issue_data.get('fields') or {}
        
        issue_info = {
            "key": issue_data.get('key', ''),
            "summary": fields.get('summary', ''),
            "description": fields.get('description', {}).get('content', []) if isinstance(fields.get('description'), dict) else fields.get('description', ''),
            "status": (fields.get('status') or {}).get('name', ''),
            "type": (fields.get('issuetype') or {}).get('name', ''),
            "assignee": (fields.get('assignee') or {}).get('displayName', 'Unassigned'),
            "reporter": (fields.get('reporter') or {}).get('displayName', ''),
            "created": fields.get('created', ''),
            "acceptance_criteria": self._extract_acceptance_criteria(fields),
            "comments": self._extract_comments(fields),
        }
        
        return issue_info

    def _extract_acceptance_criteria(self, fields: Dict) -> str:
        """Extract acceptance criteria from issue description or custom fields"""
        description = fields.get('description', {})
        if isinstance(description, dict):
            content = description.get('content', [])
            acceptance_text = ""
            for block in content:
                if 'text' in block:
                    acceptance_text += block['text'] + "\n"
            return acceptance_text.strip()
        return str(description).strip() if description else ""

    def _extract_comments(self, fields: Dict) -> list:
        """Extract comments from issue"""
        comments = []
        comment_data = (fields.get('comment') or {}).get('comments', [])
        for comment in comment_data[:5]:  # Get last 5 comments
            comments.append({
                "author": (comment.get('author') or {}).get('displayName', ''),
                "body": comment.get('body', {}).get('content', []) if isinstance(comment.get('body'), dict) else comment.get('body', ''),
                "created": comment.get('created', '')
            })
        return comments


def get_jira_connector() -> JiraConnector:
    """Factory function to get Jira connector instance"""
    return JiraConnector()
