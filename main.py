import config
import time
import datetime as dt

from datadom import DataDom
from products import Products
from email_sender import EmailSender

# Get all product data via http request in HTML DOM from Amazon
datadom = DataDom(config.watchlist, config.HEADER, config.CURRENCY_SYMBOL)
product_sets = datadom.get_all_products()

products = Products()
# Write and generate CSV file of all products
products.write_to_csv(product_sets, 'products.csv')
print(products.csv_discount_analysis('products.csv', config.discount_boundary))
# Write and generate JSON file of all products
products.write_to_json(product_sets, 'products.json')

# OPTIONAL: Create email sender and send email notifications based on discount boundary
# email_sender = EmailSender(config.EMAIL_ADDRESS, config.CURRENCY_SYMBOL)
# for product in product_sets:
#     if (product[4] >= config.discount_boundary):
#         email_sender.notify(product[0], product[1], product[2], product[3], product[4])

print("DateTime is now: {}".format(dt.datetime.now()))

# OPTIONAL: 
# while True:
#     """
#     Move code here for lazy terminal CRON job
#     """
#     time.sleep(config.TIME_INTERVAL)