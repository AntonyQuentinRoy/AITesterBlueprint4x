import { Page, Locator } from '@playwright/test';
import { config } from '../config';

export class VWOLoginPage {
    private readonly page: Page;

    // Rule 1: Use arrow function locators, avoiding CSS wrappers
    readonly usernameInput = (): Locator => this.page.getByTestId('login-username');
    readonly passwordInput = (): Locator => this.page.getByTestId('login-password');
    readonly signInButton = (): Locator => this.page.getByTestId('js-login-btn');
    readonly errorMessage = (): Locator => this.page.getByTestId('js-notification-box-msg');

    // Rule 1: Accept Page in constructor
    constructor(page: Page) {
        this.page = page;
    }

    // Rule 6: All methods must be async and return Promise
    async navigate(): Promise<void> {
        await this.page.goto(config.vwoBaseUrl);
    }

    async enterUsername(username: string): Promise<void> {
        await this.usernameInput().fill(username);
    }

    async enterPassword(password: string): Promise<void> {
        await this.passwordInput().fill(password);
    }

    async clickSignIn(): Promise<void> {
        await this.signInButton().click();
    }

    async getErrorMessageText(): Promise<string> {
        const text = await this.errorMessage().textContent();
        return text ? text.trim() : '';
    }
}
