import { defineConfig, devices } from '@playwright/test';
import * as dotenv from 'dotenv';

dotenv.config();

export default defineConfig({
    testDir: './src/tests',
    timeout: 60000,
    expect: { timeout: 10000 },
    fullyParallel: true,
    forbidOnly: !!process.env.CI,
    retries: 3, // From Migration Plan: Match TestNG maxRetryCount = 3
    workers: process.env.CI ? 2 : 3,

    reporter: [
        ['./src/utils/CustomTTAReporter.ts'],
        ['html', { open: 'never' }],
        ['json', { outputFile: 'test-results/results.json' }],
        ['list'],
    ],

    use: {
        testIdAttribute: 'id',
        baseURL: process.env.VWO_BASE_URL || 'https://app.vwo.com',
        screenshot: 'only-on-failure',
        video: 'retain-on-failure',
        trace: 'retain-on-failure',
    },

    projects: [
        { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
        { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
        { name: 'webkit', use: { ...devices['Desktop Safari'] } },
        { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
    ],
});

