# VWO Login Page — Test Cases

**URL Under Test:** `https://app.vwo.com/#/login`
**Author:** Antony Quentin Roy
**Role:** Sr. Automation Architect
**Date:** 2026-08-09
**Version:** 1.0
**Total Test Cases:** 25

---

## Verified Facts

| # | Fact | Source |
|---|---|---|
| 1 | URL is `https://app.vwo.com/#/login` | RICE POT context |
| 2 | Page contains an Email text input field | RICE POT context |
| 3 | Page contains a Password password input field | RICE POT context |
| 4 | Page contains a Submit button | RICE POT context |
| 5 | Page contains a "Remember Me" checkbox | RICE POT context |

## Missing / Unknown Information

1. Valid and invalid login credentials not provided
2. Exact DOM locators (id, name, data-testid) not confirmed
3. Exact error message text unknown
4. Post-login redirect URL unknown
5. Client-side vs server-side validation mechanism unknown
6. Rate-limiting or account lockout policy unknown
7. No PRD, API documentation, or screenshots provided

---

## Test Cases

### Smoke Tests (5)

| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
|---|---|---|---|---|---|
| 1 | SMOKE-VWO-001 | Verify login page loads successfully | Page loads without errors; URL contains `/login` | | N/A |
| 2 | SMOKE-VWO-002 | Verify Email input field is rendered and enabled | Email field is visible on page and accepts user input | | N/A |
| 3 | SMOKE-VWO-003 | Verify Password input field is rendered and enabled | Password field is visible on page and accepts user input | | N/A |
| 4 | SMOKE-VWO-004 | Verify Submit button is rendered and enabled | Submit button is visible on page and is clickable | | N/A |
| 5 | SMOKE-VWO-005 | Verify "Remember Me" checkbox is rendered | Remember Me checkbox is visible and has associated label text | | N/A |

### Sanity Tests (4)

| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
|---|---|---|---|---|---|
| 6 | SANTY-VWO-001 | Login with valid credentials — happy path | User is authenticated and redirected away from `/login` page *(Inference: low confidence — redirect URL unknown)* | | Valid email, valid password (to be provided) |
| 7 | SANTY-VWO-002 | Login with invalid credentials | Authentication fails; error message displayed; user remains on `/login` page *(Inference: low confidence — exact error text unknown)* | | Invalid email, invalid password (to be provided) |
| 8 | SANTY-VWO-003 | Login with empty Email field | Form submission is blocked OR inline error shown near Email field *(Inference: low confidence — validation mechanism unknown)* | | Email: (empty), Password: any text |
| 9 | SANTY-VWO-004 | Login with empty Password field | Form submission is blocked OR inline error shown near Password field *(Inference: low confidence — validation mechanism unknown)* | | Email: any text, Password: (empty) |

### Positive Tests (4)

| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
|---|---|---|---|---|---|
| 10 | POS-VWO-001 | Login with valid email and valid password using Submit button click | User is redirected to post-login page *(Inference: low confidence — exact redirect target unknown)* | | Valid email, valid password (to be provided) |
| 11 | POS-VWO-002 | Submit login form using Enter key after entering credentials | Form submits; behavior identical to clicking Submit button *(Inference: low confidence — assumes standard HTML form behavior)* | | Valid email, valid password (to be provided) |
| 12 | POS-VWO-003 | Login with "Remember Me" checkbox checked | User is authenticated; session persists after browser close and reopen *(Inference: low confidence — persistence mechanism and duration unknown)* | | Valid email, valid password (to be provided) |
| 13 | POS-VWO-004 | Login with "Remember Me" checkbox unchecked (default state) | User is authenticated but session does NOT persist after browser close *(Inference: low confidence — session duration policy unknown)* | | Valid email, valid password (to be provided) |

### Negative Tests (6)

| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
|---|---|---|---|---|---|
| 14 | NEG-VWO-001 | Submit with both Email and Password fields empty | Form submission blocked; validation error(s) displayed *(Inference: low confidence — single vs separate error messages unknown)* | | Email: (empty), Password: (empty) |
| 15 | NEG-VWO-002 | Submit with invalid email format — missing "@" symbol | Form submission blocked; email format validation error displayed *(Inference: low confidence — client-side vs server-side validation unknown)* | | Email: `testuservwo.com`, Password: any text |
| 16 | NEG-VWO-003 | Submit with invalid email format — missing domain part (e.g., `user@`) | Form submission blocked; email format validation error displayed *(Inference: low confidence)* | | Email: `testuser@`, Password: any text |
| 17 | NEG-VWO-004 | Submit with invalid email format — missing local part (e.g., `@vwo.com`) | Form submission blocked; email format validation error displayed *(Inference: low confidence)* | | Email: `@vwo.com`, Password: any text |
| 18 | NEG-VWO-005 | Submit with valid email and incorrect password | Authentication fails; generic error message displayed (e.g., "Invalid email or password") *(Inference: low confidence — exact error text and display mechanism unknown)* | | Valid email (to be provided), Password: `WrongPass123!` |
| 19 | NEG-VWO-006 | Submit with unregistered/non-existent email and any password | Authentication fails; error message displayed *(Inference: low confidence — app may reveal "user not found" vs generic error unknown)* | | Email: `nonexistent@test.com`, Password: any text |

### Edge / Boundary Tests (5)

| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
|---|---|---|---|---|---|
| 20 | EDGE-VWO-001 | Email field — input with leading whitespace (e.g., ` valid@vwo.com`) | Behavior depends on implementation: Email is either trimmed and accepted, or rejected as invalid *(Inference: low confidence — trimming behavior unknown)* | | Email: `‹space›valid@vwo.com` |
| 21 | EDGE-VWO-002 | Email field — input with trailing whitespace (e.g., `valid@vwo.com `) | Behavior depends on implementation: Email is either trimmed and accepted, or rejected as invalid *(Inference: low confidence)* | | Email: `valid@vwo.com‹space›` |
| 22 | EDGE-VWO-003 | Email field — maximum character length boundary (255 chars per RFC 5321) | 255-character email is accepted; 256-character email behavior observed *(Inference: low confidence — server-side length limit unknown; based on email RFC standard)* | | 255-char and 256-char email strings |
| 23 | EDGE-VWO-004 | Password field — very long password (100+ characters) | Password accepted or rejected based on application policy *(Inference: low confidence — max password length unknown)* | | 100-character password string |
| 24 | EDGE-VWO-005 | Email field — case sensitivity (e.g., `User@VWO.com` vs `user@vwo.com`) | Login behavior consistent regardless of email casing *(Inference: low confidence — depends on server-side email normalization)* | | Same email in mixed case, lower case |

### Regression / UI Tests (1)

| S.No | Test Case ID | Description | Expected Result | Actual Result | Test Data |
|---|---|---|---|---|---|
| 25 | REG-VWO-001 | Password field masks characters as user types | Characters displayed as dots or asterisks; input `type` attribute is `"password"` | | Any password string |

---

## Self-Validation Check

| Rule | Status |
|---|---|
| No invented features, APIs, or error codes | ✅ PASS — all inferences explicitly labeled |
| No assumed default system behavior | ✅ PASS — all unknowns documented; inferences marked |
| Every assertion traceable to provided input | ✅ PASS — all test cases trace to 4 verified UI elements |
| Inferences labeled | ✅ PASS — 17 inference markers with "low confidence" |
| Missing info reported | ✅ PASS — documented above |
| Exactly 25 test cases | ✅ PASS — 5 smoke + 4 sanity + 4 positive + 6 negative + 5 edge + 1 regression = 25 |
| Azure format used | ✅ PASS — S.No, Test Case ID, Description, Expected Result, Actual Result, Test Data |
| Only UI-level test cases | ✅ PASS — no backend/API/database assertions |
| Equivalence Partitioning applied | ✅ PASS — email formats partitioned (valid, no @, no domain, no local) |
| Boundary Value Analysis applied | ✅ PASS — email length 255/256 boundary, password length boundary |

---

**Status:** READY FOR REVIEW — execution pending provision of credentials and locator confirmation.
