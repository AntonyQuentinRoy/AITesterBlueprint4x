import { test, expect } from '@playwright/test';
import { VWOLoginModule } from '@modules/VWOLoginModule';
import { config } from '../config';

test.describe('VWO Login Migration Tests', () => {
    
    const loginModule = new VWOLoginModule();

    test('testFail - Should trigger intentional failure for retry and screenshot testing', async ({ page }) => {
        // Tagging matching Allure functionality
        test.info().annotations.push({ type: 'description', description: 'Verify that valid creds (Intentional failure test)' });
        
        await page.goto(config.vwoBaseUrl);
        
        // Intentional failure to match Assert.assertTrue(false)
        expect(false, 'Intentional failure to trigger retry mechanism and screenshot generation').toBeTruthy();
    });

    test('testPass - Should pass successfully', async ({ page }) => {
        test.info().annotations.push({ type: 'description', description: 'Verify that valid creds (Intentional pass test)' });
        
        await page.goto(config.vwoBaseUrl);
        
        // Intentional pass to match Assert.assertTrue(true)
        expect(true).toBeTruthy();
    });

    // An additional test actually integrating the migrated POM and Module classes
    test('should attempt login with invalid credentials using migrated Page Objects', async ({ page }) => {
        await loginModule.loginWithInvalidCredentials(page, config.invalidUser);
    });
});
