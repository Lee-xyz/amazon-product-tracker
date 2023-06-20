import csv
import json
import pandas as pd

class Products():
    def __init__(self):
        return None
    
    def write_to_csv(self, product_set, csv_file):
        header = ['url', 'name', 'rrp', 'current_price', 'discount']
        products_data = product_set

        with open(csv_file, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(products_data)

    def csv_discount_analysis(self, csv_file, discount_boundary):
        desired_discount_products = []
        df = pd.read_csv(csv_file)
        df_sorted = df.sort_values(by=["discount"], ascending=False)

        for row in df.itertuples():
            if row.discount >= discount_boundary:
                desired_discount_products.append(row.url)

        print("\n\nThere are currently {}".format(len(desired_discount_products)) + " product(s) over or equal to {}".format(discount_boundary * 100) + "% off:")
        return df_sorted
    
    def write_to_json(self, product_set, json_file):
        product_set_to_json = []

        for product in product_set:
            product_set_to_json.append({'product_url': product[0], 'product_name': product[1], 'product_rrp': product[2], 'product_current_price': product[3], 'product_discount': product[4]})
        
        with open(json_file, 'w') as f:
            json.dump(product_set_to_json, f)