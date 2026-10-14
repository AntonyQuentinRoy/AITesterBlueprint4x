import { Page, expect } from '@playwright/test';
import { VWOLoginPage } from '@pages/VWOLoginPage';
import { VWOUserCredentials } from '../testdata/types';

export class VWOLoginModule {
    // Rule 2: Modules: Accept `Page` as METHOD parameter (NOT constructor)
    
    async loginWithInvalidCredentials(page: Page, user: VWOUserCredentials): Promise<void> {
        const loginPage = new VWOLoginPage(page);
        
        await loginPage.navigate();
        await loginPage.enterUsername(user.username);
        
        if (user.password) {
            await loginPage.enterPassword(user.password);
        }
        
        await loginPage.clickSignIn();
        
        // Rule 9 & 10: NO Thread.sleep, rely on auto-wait. Use expect()
        await expect(loginPage.errorMessage()).toBeVisible();
        const errorText = await loginPage.getErrorMessageText();
        
        if (user.expectedError) {
            expect(errorText).toContain(user.expectedError);
        }
    }

    async loginWithValidCredentials(page: Page, user: VWOUserCredentials): Promise<void> {
        const loginPage = new VWOLoginPage(page);
        
        await loginPage.navigate();
        await loginPage.enterUsername(user.username);
        
        if (user.password) {
            await loginPage.enterPassword(user.password);
        }
        
        await loginPage.clickSignIn();
        
        // Check implicitly for navigation away from login
        await expect(page).not.toHaveURL(/.*login/);
    }
}
