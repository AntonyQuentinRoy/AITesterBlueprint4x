# Understanding the RICE POT Prompt - Test Case

Here's what I extract from this prompt before I build the Test cases:

**The RICE POT template** is a structured prompting framework for generating enterprise-grade code with zero ambiguity. This specific instance asks for a login page** using:

| Layer | What it Demands |
|---|---|
| **Role** | QA architect with 15yrs domain expertise |
| **Instructions** | Enterprise quality test case covering postivie,negative,edge,regression,smoke,sanity test cases |
| **Context** | `https://app.vwo.com/#/login` — email, password, submit,"remember me" |
| **Example** | Parameters should be the test case paramters from Azure ADO | 
| **Parameters** |Login Credentials,Equivilance Partition and Boundary Value Analysis for test data |
| **Output** | Exactly 25 test cases: '\asset\prompt_docs\TestCases\|
| **Tone** | Premium,Azure format template,Only UI cases|

**Sample Header Format**
| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
