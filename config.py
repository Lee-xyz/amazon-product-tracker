# HTTP request header
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

# OPTIONAL: Time interval for price updates (in seconds) - 1 week default
TIME_INTERVAL = 24 * 60 * 60 * 7

# OPTIONAL: Your email credentials
EMAIL_ADDRESS = "your-email-address@gmail.com"

# Your local currency symbol
CURRENCY_SYMBOL = "£"

# Add your amazon products here {url*x* : amazon_link} - where *x* is a unique number
watchlist = {'url1': 'https://www.amazon.co.uk/Logitech-Wireless-Lightweight-Programmable-compatible/dp/B07G5XJLWK/ref=sr_1_8?keywords=logitech+mouse&qid=1687130813&sprefix=logitech%2Caps%2C72&sr=8-8',
            'url2': 'https://www.amazon.co.uk/Sennheiser-Wireless-Headphones-active-cancellation-Black/dp/B083T4XJDY/ref=sr_1_6?keywords=headphones+sennheiser&qid=1687130881&sprefix=headphones+se%2Caps%2C76&sr=8-6',
            'url3': 'https://www.amazon.co.uk/Corsair-CH-9115020-UK-Key-Less-Mechanical-Keyboard/dp/B06XQ5G9ZZ/ref=sr_1_22?keywords=keyboard+mechanical&qid=1687130924&sprefix=keyboard+mech%2Caps%2C74&sr=8-22'}

# Enter your desired discount percentage (0.20 = 20%)
discount_boundary = 0.20