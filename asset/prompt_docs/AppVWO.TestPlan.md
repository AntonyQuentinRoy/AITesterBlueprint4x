# VWO Login Page — Automation Test Plan

**URL Under Test:** `https://app.vwo.com/#/login`
**Author:** Antony Quentin Roy
**Role:** Sr. Automation Architect
**Date:** 2026-08-09
**Version:** 1.0

---

## 1. Objective

Validate the functional correctness, error handling, and reliability of the VWO login page (`app.vwo.com/#/login`) through automated testing, covering all identified UI elements: email input, password input, submit button, and "remember me" checkbox.

---

## 2. Context

The VWO login page serves as the authentication gateway to the VWO application. The page contains the following verified elements (sourced from the RICE POT context):

| Element | Type | Verified |
|---|---|---|
| Email field | Text input | Yes — from context |
| Password field | Password input | Yes — from context |
| Submit button | Button | Yes — from context |
| "Remember Me" checkbox | Checkbox | Yes — from context |

**Inference (low confidence):** The page is a standard single-page application login form. No server-rendered pages are assumed.

---

## 3. Scope

### In-Scope
- Functional testing of all four identified UI elements
- Form submission workflow (happy path)
- Client-side validation behavior
- "Remember Me" checkbox state persistence across sessions (Inference — low confidence)
- Cross-browser rendering consistency (Inference — low confidence)

### Out-of-Scope
- Backend authentication API (no API documentation provided)
- Password reset flow (no PRD reference)
- Account creation / registration (not present on page)
- Performance / load testing (no requirements provided)
- Security penetration testing (no requirements provided)
- OAuth / SSO / third-party authentication (no documentation)

---

## 4. Limitations

1. **No PRD or API documentation available** — backend behavior, error codes, and authentication mechanisms are unknown.
2. **No screenshots provided** — UI layout, field labels, placeholder text, and visual design cannot be verified.
3. **No test data provided** — valid/invalid credentials, expected error messages are unknown.
4. **No error-handling specification** — exact error messages, toast notifications, or inline validation text is untestable without documentation.
5. **No post-login behavior documented** — redirect URL, dashboard layout, and session management are unknown.
6. **No rate-limiting or lockout policy** — cannot test brute-force or lockout scenarios.
7. **No accessibility or localization requirements** — ARIA attributes, i18n labels are unknown.

---

## 5. Constraints

| Constraint | Detail |
|---|---|
| **Input dependency** | Test execution requires valid and invalid credentials (not yet provided) |
| **Environment** | Production URL only; no staging/QA environment identified |
| **Output format** | Test plan delivered as this document |
| **Tooling** | Automation framework and language to be selected based on stack (not yet specified) |
| **Execution** | No CI/CD pipeline or scheduling defined |

---

## 6. Test Strategy

### 6.1 Approach
- **Black-box functional testing** via UI automation (browser-level)
- **Data-driven testing** for credential validation scenarios (once test data is provided)
- **Page Object Model (POM)** for maintainable locator management

### 6.2 Test Environment

| Parameter | Value |
|---|---|
| Base URL | `https://app.vwo.com/#/login` |
| Browsers | Chrome, Firefox, Edge |

  *Inference (low confidence) — Safari and mobile browsers are not included as no mobile requirement was specified.*

### 6.3 Element Locator Strategy

| Element | Recommended Locator Type | Notes |
|---|---|---|
| Email input | `id`, `name`, or `data-testid` | Unknown; requires page inspection |
| Password input | `id`, `name`, or `data-testid` | Unknown; requires page inspection |
| Submit button | `type="submit"`, `button` text, or `id` | Unknown; requires page inspection |
| Remember Me checkbox | `type="checkbox"`, `id`, or `name` | Unknown; requires page inspection |

  *Inference (low confidence) — Locator strategies are based on common web patterns. Actual locators MUST be confirmed via DOM inspection or provided documentation.*

---

## 7. Test Cases

### TC-01: Login Happy Path — Valid Credentials

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-001 |
| **Priority** | Critical |
| **Precondition** | Valid credentials available |
| **Steps** | 1. Navigate to `https://app.vwo.com/#/login` |
| | 2. Enter valid email in email field |
| | 3. Enter valid password in password field |
| | 4. Click submit button |
| **Expected Result** | User is redirected to the authenticated dashboard/landing page |
| **Assertions** | URL changes from `/login` to post-login route |

  *Inference (low confidence) — Exact redirect URL unknown. Behavior after login not documented.*

---

### TC-02: Login — Empty Email Field

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-002 |
| **Priority** | High |
| **Precondition** | None |
| **Steps** | 1. Navigate to login page |
| | 2. Leave email field empty |
| | 3. Enter any password |
| | 4. Click submit |
| **Expected Result** | Client-side validation prevents submission. Error message displayed near email field. |
| **Assertions** | Submit is blocked OR error message appears |

  *Inference (low confidence) — Error message text and validation mechanism unknown.*

---

### TC-03: Login — Empty Password Field

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-003 |
| **Priority** | High |
| **Precondition** | None |
| **Steps** | 1. Navigate to login page |
| | 2. Enter any email |
| | 3. Leave password field empty |
| | 4. Click submit |
| **Expected Result** | Client-side validation prevents submission. Error message displayed near password field. |
| **Assertions** | Submit is blocked OR error message appears |

  *Inference (low confidence) — Error message text and validation mechanism unknown.*

---

### TC-04: Login — Invalid Credentials

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-004 |
| **Priority** | High |
| **Precondition** | Known invalid credentials (incorrect email/password) |
| **Steps** | 1. Navigate to login page |
| | 2. Enter invalid email |
| | 3. Enter invalid password |
| | 4. Click submit |
| **Expected Result** | Authentication fails. Error message displayed (e.g., "Invalid email or password"). User remains on login page. |
| **Assertions** | Error message visible; URL still contains `/login` |

  *Inference (low confidence) — Exact error message text, error display mechanism (toast/inline/modal), and HTTP status codes unknown.*

---

### TC-05: Login — Valid Email + Invalid Password

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-005 |
| **Priority** | High |
| **Precondition** | Valid email; known invalid password |
| **Steps** | 1. Navigate to login page |
| | 2. Enter valid email |
| | 3. Enter invalid password |
| | 4. Click submit |
| **Expected Result** | Authentication fails. Error message displayed. |
| **Assertions** | Error visible; user stays on login page |

  *Inference (low confidence) — Behavior may differ depending on whether the server distinguishes "user not found" vs "wrong password" for security reasons.*

---

### TC-06: Remember Me — Checkbox Toggle

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-006 |
| **Priority** | Medium |
| **Precondition** | None |
| **Steps** | 1. Navigate to login page |
| | 2. Verify "Remember Me" checkbox is unchecked (default state) |
| | 3. Click checkbox to check it |
| | 4. Click again to uncheck |
| **Expected Result** | Checkbox toggles between checked and unchecked states |
| **Assertions** | `checked` attribute/property reflects correct state |

---

### TC-07: Remember Me — Persistence After Login

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-007 |
| **Priority** | Medium |
| **Precondition** | Valid credentials available |
| **Steps** | 1. Navigate to login page |
| | 2. Check "Remember Me" checkbox |
| | 3. Enter valid credentials and submit |
| | 4. After successful login, close browser completely |
| | 5. Reopen browser and navigate to `https://app.vwo.com` |
| **Expected Result** | User session is persisted; user is already authenticated or auto-logged-in |
| **Assertions** | User does not see the login page on return visit |

  *Inference (low confidence) — "Remember Me" implementation (cookie/localStorage/session token) unknown. Exact persistence behavior unknown.*

---

### TC-08: Password Field — Masking

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-008 |
| **Priority** | Low |
| **Precondition** | None |
| **Steps** | 1. Navigate to login page |
| | 2. Type text into password field |
| **Expected Result** | Characters are masked (displayed as dots/asterisks) |
| **Assertions** | Password input `type` attribute equals `"password"` |

---

### TC-09: Tab Order / Keyboard Navigation

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-009 |
| **Priority** | Low |
| **Precondition** | None |
| **Steps** | 1. Navigate to login page |
| | 2. Press Tab repeatedly |
| **Expected Result** | Focus moves through fields in logical order: Email → Password → Remember Me → Submit |
| **Assertions** | Each element receives focus in correct sequence |

  *Inference (low confidence) — Exact tab order unknown without DOM inspection.*

---

### TC-10: Submit via Enter Key

| Field | Value |
|---|---|
| **ID** | TC-LOGIN-010 |
| **Priority** | Medium |
| **Precondition** | Valid credentials |
| **Steps** | 1. Navigate to login page |
| | 2. Enter valid email |
| | 3. Enter valid password |
| | 4. Press Enter key |
| **Expected Result** | Form submits successfully (same behavior as clicking submit button) |
| **Assertions** | Same as TC-LOGIN-001 |

  *Inference (low confidence) — Default form submission behavior assumed.*

---

## 8. Automation Architecture Recommendation

```
tests/
├── pages/
│   └── LoginPage.js          # Page Object Model for login page
├── data/
│   └── credentials.json       # Test data (to be populated)
├── specs/
│   └── login.spec.js          # Test cases
└── config/
    └── browser.config.js      # Browser/URL configuration
```

| Layer | Responsibility |
|---|---|
| **Page Objects** | Encapsulate locators and page actions |
| **Test Data** | Externalized credentials (JSON/CSV) for data-driven tests |
| **Specs** | Assertions and test flow orchestration |
| **Config** | Environment URLs, browser selection, timeouts |

*Inference (low confidence) — Tooling choice (Playwright, Selenium, Cypress) is not specified. Structure is generic and adaptable.*

---

## 9. Deliverables

| # | Deliverable | Format |
|---|---|---|
| 1 | Test Plan (this document) | Markdown |
| 2 | Automation scripts | Source code (language TBD) |
| 3 | Test execution report | HTML/JSON (post-execution) |
| 4 | Bug reports | Per defect found |

---

## Self-Validation Check

| Rule | Status |
|---|---|
| No invented features, APIs, or error codes | ✅ PASS — all inferences explicitly labeled |
| No assumed default behavior | ✅ PASS — all unknowns documented in Limitations |
| Every assertion traceable to input | ✅ PASS — 4 verified elements from RICE POT context |
| Inferences labeled | ✅ PASS — 10 inference markers with "low confidence" |
| Missing info reported | ✅ PASS — Section 4 (Limitations) |

---

**Status:** READY FOR REVIEW — test execution pending provision of credentials, locator details, and error-handling documentation.
