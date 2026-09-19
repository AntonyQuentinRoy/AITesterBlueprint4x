# Understanding the RICE POT Prompt - Steps to build a Langflow for flaky test cases generation

Here's what I extract from this prompt before I build the Test cases:

**The RICE POT template** is a structured prompting framework for generating enterprise-grade code with zero ambiguity. This specific instance asks for a login page** using:

| Layer | What it Demands |
|---|---|
| **Role** | QA architect with 15yrs domain expertise |
| **Instructions** | To read the folder from path chapter9_langflow\Playwright_Report1 and chapter9_langflow\Playwright_Report2 which contains all the results json files and tell me which test cases and how many tests are flaky and a json to create the langflow model which has the user input chat and other components to generate the output to the user |
| **Context** | A Langflow model for flaky test case generation |
| **Example** | Json to be used for creating the langflow model | 
| **Parameters** | |
| **Output** | chapter9_langflow\Playwright_Results\Langflow_FlakyTCFinder_Model.json |
| **Tone** | Premium component to create a langflow |

**Sample json Format**
| chapter9_langflow\Flaky Testcase finder.json |
