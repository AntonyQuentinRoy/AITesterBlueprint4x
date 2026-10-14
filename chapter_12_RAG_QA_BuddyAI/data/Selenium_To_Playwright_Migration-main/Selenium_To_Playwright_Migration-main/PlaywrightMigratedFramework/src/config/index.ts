import * as dotenv from 'dotenv';
import { VWOUserCredentials } from '../testdata/types';

// Load environment variables
dotenv.config();

export interface AppConfig {
    vwoBaseUrl: string;
    validUser: VWOUserCredentials;
    invalidUser: VWOUserCredentials;
    logLevel: string;
    environment: string;
}

/**
 * Application configuration loaded from environment variables
 * Replaces PropertiesReader and data.properties entirely
 */
export const config: AppConfig = {
    vwoBaseUrl: process.env.VWO_BASE_URL || 'https://app.vwo.com',
    
    // VWO Valid credentials mapped from properties
    validUser: {
        username: process.env.VWO_USERNAME || 'hebiva4776@amcret.com',
        password: process.env.VWO_PASSWORD || 'Test@4321',
    },
    
    // VWO Invalid credentials + expected error message natively handled
    invalidUser: {
        username: process.env.VWO_INVALID_USERNAME || 'admin@admin.com',
        password: process.env.VWO_INVALID_PASSWORD || 'Test@2024',
        expectedError: process.env.VWO_ERROR_MESSAGE || 'Your email, password, IP address or location did not match',
    },
    
    logLevel: process.env.LOG_LEVEL || 'INFO',
    environment: process.env.TEST_ENV || 'QA',
};

export default config;
