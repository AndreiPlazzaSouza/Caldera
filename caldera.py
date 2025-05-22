import asyncio
from pyppeteer import launch

async def create_wallet():
    browser = await launch(headless=True)  # headless=True for cronjob
    page = await browser.newPage()
    
    # Navigate to Caldera wallet creation page
    await page.goto('https://caldera.example.com/create-wallet')  # Replace with actual URL
    
    # Wait for and click "Create Wallet" button
    await page.waitForSelector('button#create-wallet')  # Replace selector
    await page.click('button#create-wallet')
    
    # Wait for seed phrase or wallet info to appear
    await page.waitForSelector('.seed-phrase')  # Replace selector
    
    # Extract seed phrase text
    seed_phrase = await page.evaluate('''() => {
        return document.querySelector('.seed-phrase').innerText;
    }''')
    
    print("Wallet Seed Phrase:", seed_phrase)
    
    # Optionally save seed phrase to file
    with open('wallet_seed.txt', 'a') as f:
        f.write(seed_phrase + '\n')
    
    await browser.close()

if __name__ == '__main__':
    asyncio.run(create_wallet())
