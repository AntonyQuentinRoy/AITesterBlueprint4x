# Selenium to Playwright Migration - Ultimate AI-Assisted Base Framework

This repository represents a complete pipeline and target architecture used to migrate a legacy **Java / Selenium / TestNG** project to a modern **TypeScript / Playwright** framework. 

## 📚 Essential Resources & Documentation
- [Selenium to Playwright Migration Tutorial (The Testing Academy)](https://app.thetestingacademy.com/selenium-to-playwright-migration-tutorial)
- [Playwright MCP Guide](https://www.youtube.com/watch?v=Y3sGRc_WFfc&t=2371s)
- [Playwright AI Agents](https://www.youtube.com/watch?v=5IW5ny1L2Qg&t=781s)
- [Playwright CLI](https://www.youtube.com/watch?v=DcFQOJEIgsI&t=1s)

## 🛠️ Part 1 - Prerequisites & Setup Guide

Ensure your development environment matches the baseline definitions below before executing tests:
- **[Node.js >= 18 & npm >= 9 installed](https://nodejs.org/en/download)**
- **[VS Code with Playwright extension](https://code.visualstudio.com/download)**
- **[Git installed & configured](https://git-scm.com/install/)**
- **Basic TypeScript knowledge** (types, interfaces, async/await functionality)
- **Familiarity with the Baseline Selenium Java Framework** structure.

---

## 🏗️ Migration Architecture & Strategy

We utilized a rigorous **3-Layer Architecture** replacing the heavy Base Class legacy structure used in TestNG:
1. **Pages Layer (`src/pages`)**: Strictly typed Page Objects utilizing arrow-function accessors and native `getByRole` or `getByTestId` locator strategies.
2. **Modules Layer (`src/modules`)**: Stateless components mapping directly to business logic workflows (e.g., `loginWithInvalidCredentials(page, user)`), explicitly stripping state storage out of the Module classes.
3. **Test specifications (`src/tests`)**: Replacing JUnit/TestNG classes natively with Playwright's describe/test runner mapping auto-awaited `expect()` assertions.

### Core Component Migrations
| Legacy Selenium Tool | Modern Playwright Ecosystem |
| --- | --- |
| `pom.xml` / `testng.xml` | `package.json` / `playwright.config.ts` |
| `data.properties` / `PropertiesReader.java` | `.env` / `src/config/index.ts` |
| `@RetryAnalyzer` & `ScreenshotListener` | Natively Handled via `retries: 3` & `use: { screenshot: 'only-on-failure' }` |
| **Allure Analytics** | `CustomTTAReporter.ts` & Playwright HTML Reports |
| **`By.xpath` / CSS Wrappers** | `getByTestId()` mapped to `testIdAttribute: 'id'` |
| **Apache POI (Excel)** | JSON data-driven testing with strict TypeScript Interfaces |
| **`Thread.sleep(x)`** | `await expect(locator).toBeVisible()` |

---

## 🚀 Execution Guide

1. **Install Dependencies Check**
   ```bash
   cd PlaywrightMigratedFramework
   npm install
   npx playwright install chromium --with-deps
   ```

2. **Environment Variable Configuration**
   By default, the framework utilizes the `src/config/index.ts` mapping and pulls `.env` configurations. Copy `.env` to ensure `VWO_BASE_URL` and credential aliases are configured securely.

3. **Running the Migrated Tests**
   ```bash
   npx playwright test
   ```

4. **Generating Quality Assessment Reports**
   The architecture integrates the Custom TTA Reporter natively, logging history, and generating comprehensive `.html` reports located inside the `tta-report/` directory containing traced screenshots and trace viewer zip links natively.

---
Created by Pramod Dutta  
[TheTestingAcademy](https://thetestingacademy.com) | [GitHub](https://github.com/PramodDutta) | [LinkedIn](https://linkedin.com/in/pramoddutta)
