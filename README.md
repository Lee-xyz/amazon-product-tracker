# Introduction
This script generates a JSON and CSV file based on the user's defined Amazon watchlist on tracked products. In addition, it can send emails to remind you of products currently on discount (gmail required). Perfect for periodically updating product details without manual checking using CRON and serving as a back-end API.

Product information then includes the following specified headers: url, name, rrp, price, and discount.
Examples of generated JSON and CSV file content can be previewed below for an example product:
```
JSON Format:
{"product_url": "https://www.amazon.co.uk/Sennheiser-Wireless-Headphones-active-cancellation-Black/dp/B083T4XJDY/ref=sr_1_6?keywords=headphones+sennheiser&qid=1687130881&sprefix=headphones+se%2Caps%2C76&sr=8-6", "product_name": "Sennheiser HD 450BT Wireless Headphones, with active noise cancellation, Black", "product_rrp": 159.0, "product_current_price": 119.0, "product_discount": 0.25}

CSV Format:
url,name,rrp,current_price,discount
https://www.amazon.co.uk/Sennheiser-Wireless-Headphones-active-cancellation-Black/dp/B083T4XJDY/ref=sr_1_6?keywords=headphones+sennheiser&qid=1687130881&sprefix=headphones+se%2Caps%2C76&sr=8-6,"Sennheiser HD 450BT Wireless Headphones, with active noise cancellation, Black",159.0,119.0,0.25
```

# Install packages
Requires [Python](https://www.python.org/downloads/)
```
pip install -r requirements.txt
```

# Update config
Go to [config.py](/config.py) and update the following variables:
```
CURRENCY_SYMBOL - str: Your local currency symbol (that appears on the Amazon website)
EMAIL_ADDRESS - str: Your email address
TIME_INTERVAL - int: Duration in seconds for scheduling function jobs
watchlist - dict: Your product watchlist in the form url*x* : amazon_url, where *x* is a unique number
discount_boundary - float: Desired discount boundary in 2f form, e.g. 0.20 = 20% discount
```

# Run
```
cd your-installation-folder
./main.py
```

# Setting up Gmail Auth
For the email sender module using gmail services to work, you must follow these steps below before running: [\[see this blog for more in-depth information\]](https://mailtrap.io/blog/python-send-email-gmail/).

1. Create your [Google Cloud Project](https://console.cloud.google.com/projectcreate) and select the Project
2. Go to your [Google API \& Services dashboard](https://console.cloud.google.com/apis/dashboard). You will see several tabs on the left.
    - Head to Library > Search for "Gmail API" > Enable Gmail API
    - Head to Credentials > Create New Credentials > OAuth Client ID > Select Desktop App Type and create > Head back to download OAuth client (.json) > Rename your json file to "credentials.json" and place it in your root project repository 
    - Head to OAuth consent screen > Scroll down to Test Users section and click Add Users > Add your email address and save
3. Update the EMAIL_ADDRESS variable in [config.py](/config.py), if not done so already.
4. Sign into Google OAuth v2 when required when running [main.py](/main.py) to complete authentication flow.

# Notes
For test units, see [test_units.py](/test_units.py) for object class and function use-cases. This test file uses the same configuration settings from [config.py](/config.py) to ensure object classes, functions, and output files are as expected when running the same configuration settings on main.