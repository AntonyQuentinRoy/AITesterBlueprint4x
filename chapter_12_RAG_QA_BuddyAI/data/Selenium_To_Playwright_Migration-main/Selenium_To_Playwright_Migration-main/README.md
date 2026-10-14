# Selenium to Playwright Migration Project

A complete migration of an advanced Java/Selenium/TestNG test automation framework to TypeScript/Playwright, demonstrating enterprise-grade migration patterns and best practices.

**Tutorial Reference:** [Selenium to Playwright Migration Tutorial](https://app.thetestingacademy.com/selenium-to-playwright-migration-tutorial) by [The Testing Academy](https://thetestingacademy.com)

---

## Project Structure

```
Selenium2PlaywrightMigration/
├── ATB13xSeleniumAdvanceFramework/     # Original Java/Selenium/TestNG Framework
├── Advance-Playwright-Framework/        # Reference Playwright Framework (Architecture Guide)
└── PlaywrightMigratedFramework/         # Migrated TypeScript/Playwright Framework
```

---

## Migration Summary

| Aspect | Before (Selenium) | After (Playwright) |
|--------|-------------------|-------------------|
| **Language** | Java | TypeScript |
| **Test Runner** | TestNG | Playwright Test |
| **Build Tool** | Maven (`pom.xml`) | npm (`package.json`) |
| **Configuration** | `data.properties` + `PropertiesReader.java` | `.env` + `src/config/index.ts` |
| **Browser Management** | `DriverManager.java` (65 lines) | Built-in (0 lines) |
| **Retry Logic** | `RetryAnalyzer.java` + `RetryListener.java` (34 lines) | `retries: 3` in config (1 line) |
| **Screenshots** | `ScreenshotListener.java` (53 lines) | `screenshot: 'only-on-failure'` (1 line) |
| **Reporting** | Allure Reports | Native HTML + Custom TTA Reporter |
| **Wait Utilities** | `WebDriverWait` + `FluentWait` | Auto-wait (built-in) |
| **Parallelism** | TestNG + Selenium Grid | Native workers + Browser isolation |
| **Locators** | `By.id()`, `By.xpath()` | `getByTestId()`, `getByRole()` |
| **Test Data** | Apache POI (Excel) | JSON files |

### Lines of Boilerplate Eliminated: ~244 lines

---

## Test Case Migrated

**Original:** `TestVWOLogin_05_TakeScreen_Retry_Prop_Improved_POM.java`

| Test Method | Description | Selenium | Playwright |
|-------------|-------------|----------|------------|
| `testFail()` | Intentional failure to test retry & screenshot capture | `Assert.assertTrue(false)` | `expect(false).toBeTruthy()` |
| `testPass()` | Validates test execution passes | `Assert.assertTrue(true)` | `expect(true).toBeTruthy()` |
| `loginWithInvalidCredentials()` | Tests login with invalid credentials using Page Objects | Manual implementation | Migrated POM + Module pattern |

---

## Migrated Framework Architecture

### Layered Architecture (Pages -> Modules -> Tests)

```
PlaywrightMigratedFramework/
├── .env                              # Environment variables (VWO credentials)
├── playwright.config.ts              # Playwright configuration
├── package.json                      # Dependencies & scripts
├── tsconfig.json                     # TypeScript configuration
└── src/
    ├── config/
    │   └── index.ts                  # Centralized config (replaces PropertiesReader)
    ├── pages/
    │   └── VWOLoginPage.ts           # Page Object with arrow function locators
    ├── modules/
    │   └── VWOLoginModule.ts         # Business logic layer (stateless)
    ├── testdata/
    │   └── types.ts                  # TypeScript interfaces
    ├── tests/
    │   └── vwo-login.spec.ts         # Migrated test specifications
    └── utils/
        ├── CustomTTAReporter.ts      # Custom HTML Reporter (1900+ lines)
        ├── Logger.ts                 # Logging utility
        ├── WaitHelper.ts             # Wait utilities
        └── ApiHelper.ts              # API helper utilities
```

---

## Key Migration Patterns Applied

### 1. Page Object Pattern

**Selenium (Java):**
```java
public class LoginPage extends CommonToAllPage {
    @FindBy(id = "login-username")
    WebElement usernameInput;

    public void enterUsername(String username) {
        usernameInput.sendKeys(username);
    }
}
```

**Playwright (TypeScript):**
```typescript
export class VWOLoginPage {
    constructor(private readonly page: Page) {}

    // Arrow function locators (lazy evaluation)
    readonly usernameInput = (): Locator => this.page.getByTestId('login-username');

    async enterUsername(username: string): Promise<void> {
        await this.usernameInput().fill(username);
    }
}
```

### 2. Module Pattern (Business Logic Layer)

**Key Rule:** Modules accept `Page` as a **method parameter**, not in constructor.

```typescript
export class VWOLoginModule {
    async loginWithInvalidCredentials(page: Page, user: VWOUserCredentials): Promise<void> {
        const loginPage = new VWOLoginPage(page);
        await loginPage.navigate();
        await loginPage.enterUsername(user.username);
        await loginPage.clickSignIn();
        await expect(loginPage.errorMessage()).toBeVisible();
    }
}
```

### 3. Configuration Migration

**Selenium:** `data.properties` + `PropertiesReader.java`
```properties
browser=chrome
url=https://app.vwo.com
username=admin@admin.com
```

**Playwright:** `.env` + `src/config/index.ts`
```typescript
export const config: AppConfig = {
    vwoBaseUrl: process.env.VWO_BASE_URL || 'https://app.vwo.com',
    validUser: {
        username: process.env.VWO_USERNAME || 'user@example.com',
        password: process.env.VWO_PASSWORD || 'password',
    },
};
```

### 4. Retry & Screenshot Configuration

**Selenium:** 3 Java files (RetryAnalyzer, RetryListener, ScreenshotListener)

**Playwright:** Single config file
```typescript
export default defineConfig({
    retries: 3,
    use: {
        screenshot: 'only-on-failure',
        video: 'retain-on-failure',
        trace: 'retain-on-failure',
    },
});
```

### 5. Locator Strategy Migration

| Selenium | Playwright |
|----------|------------|
| `By.id("login-username")` | `page.getByTestId('login-username')` |
| `By.xpath("//button[text()='Login']")` | `page.getByRole('button', { name: 'Login' })` |
| `By.cssSelector(".error-msg")` | `page.getByTestId('error-message')` |
| `By.linkText("Dashboard")` | `page.getByRole('link', { name: 'Dashboard' })` |

---

## What Gets Eliminated

| Selenium Component | Lines | Playwright Replacement |
|--------------------|-------|----------------------|
| `DriverManager.java` | 65 | Built-in browser management |
| `DriverManagerTL.java` | 8 | Built-in parallel isolation |
| `CommonToAllTest.java` | 21 | Playwright fixtures |
| `RetryAnalyzer.java` | 18 | `retries: 3` (config) |
| `RetryListener.java` | 16 | Not needed |
| `ScreenshotListener.java` | 53 | `screenshot: 'only-on-failure'` |
| `TakeScreenShot.java` | 43 | `page.screenshot()` built-in |
| `log4j2.xml` | 20 | `Logger.ts` utility |
| **Total** | **244** | **~10 lines of config** |

---

## Running the Migrated Tests

### Prerequisites
- Node.js 18+
- npm 9+

### Installation
```bash
cd PlaywrightMigratedFramework
npm install
npx playwright install
```

### Run Tests
```bash
# Run all tests
npm test

# Run with UI mode
npm run test:ui

# Run headed (see browser)
npm run test:headed

# Run specific browser
npm run test:chromium
npm run test:firefox
npm run test:webkit

# Run with debug
npm run test:debug

# View report
npm run test:report
```

### Available Scripts
| Script | Description |
|--------|-------------|
| `npm test` | Run all tests |
| `npm run test:headed` | Run with visible browser |
| `npm run test:ui` | Open Playwright UI mode |
| `npm run test:debug` | Debug mode with inspector |
| `npm run test:chromium` | Run on Chromium only |
| `npm run test:firefox` | Run on Firefox only |
| `npm run test:webkit` | Run on WebKit only |
| `npm run test:mobile` | Run on mobile Chrome emulation |
| `npm run test:smoke` | Run tests tagged @Smoke |
| `npm run test:p0` | Run tests tagged @P0 |
| `npm run test:report` | Open HTML report |

---

## Custom TTA Reporter Features

The migrated framework includes a custom HTML reporter (`CustomTTAReporter.ts`) with:

- Real-time report updates (auto-refresh every 5 seconds during execution)
- Statistics dashboard (Total, Passed, Failed, Skipped, Pass Rate)
- Environment and browser information
- Expandable test details with:
  - Error messages and stack traces
  - Step-by-step execution timeline
  - Video timestamps for each step
  - Console logs per step
  - Screenshots (automatic on failure)
- Interactive video player with trace viewer integration
- Filter by status (Passed/Failed/Skipped)
- Filter by priority tags (P0/P1/Smoke)
- Report history with timestamped archives

---

## Concept Mapping Reference

| Selenium/TestNG | Playwright |
|-----------------|------------|
| `WebDriver` | `page` (injected) |
| `@BeforeMethod` | `test.beforeEach()` or fixtures |
| `@AfterMethod` | `test.afterEach()` or fixtures |
| `@Test` | `test('name', async ({page}) => {})` |
| `@Listeners` | Config options |
| `Assert.assertTrue()` | `expect(...).toBeTruthy()` |
| `Assert.assertEquals()` | `expect(...).toEqual()` |
| `getDriver().get(url)` | `page.goto(url)` |
| `Thread.sleep()` | Auto-wait (discouraged: `page.waitForTimeout()`) |
| `WebDriverWait` | Built-in auto-waiting |
| `TestNG suite XML` | `playwright.config.ts` projects |
| `Allure @Owner` | `test.info().annotations` |
| `pom.xml` | `package.json` |

---

## CI/CD Integration

The framework supports:

- **Jenkins Pipeline:** `Jenkinsfile` with sharding support (`--shard=$SHARD/$SHARD_COUNT`)
- **Docker:** `docker-compose.yml` for containerized execution
- **GitHub Actions:** Ready for integration
- **Parallel Execution:** Native worker support with browser isolation

---

## Migration Acceptance Criteria (All Passed)

- [x] `npx playwright test src/tests/vwo-login.spec.ts` runs successfully
- [x] `testPass` equivalent passes on first attempt
- [x] `testFail` equivalent fails, is retried 3 times, then marked as failed
- [x] Screenshot automatically captured for failed tests
- [x] Logger output appears in console during execution
- [x] VWO URL and credentials read from `.env`
- [x] Layered architecture maintained: `config/` -> `utils/` -> `pages/` -> `modules/` -> `tests/`
- [x] No Selenium/TestNG imports in migrated code
- [x] Native HTML report + Custom TTA Report generated
- [x] Locators use semantic `getByTestId()` pattern
- [x] Test data uses JSON instead of Excel

---

## Dependencies

```json
{
  "devDependencies": {
    "@playwright/test": "^1.57.0",
    "@types/node": "^25.0.6",
    "dotenv": "^17.2.3",
    "typescript": "^5.9.3"
  }
}
```

**Comparison:** Selenium framework required 10+ dependencies (Selenium, TestNG, WebDriverManager, Allure, Apache POI, Log4j2, etc.)

---

## Author

**Pramod Dutta** - [The Testing Academy](https://thetestingacademy.com)

---

## License

ISC

---

## Resources

- [Selenium to Playwright Migration Tutorial](https://app.thetestingacademy.com/selenium-to-playwright-migration-tutorial)
- [Playwright Documentation](https://playwright.dev)
- [The Testing Academy](https://thetestingacademy.com)
