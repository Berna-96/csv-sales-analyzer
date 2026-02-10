from utils import average_price

import csv

products = []
prices = []
quantities = []

with open("data/sales.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        products.append(row["product"])
        prices.append(float(row["price"]))
        quantities.append(int(row["quantity"]))


print("Total revenue:", total_revenue(prices, quantities))
print("Average price:", average_price(prices))
print("Best product:", best_product(products, prices, quantities))
print("Total items sold:", total_items_sold(quantities))

with open("data/report.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["metric", "value"])
    writer.writerow(["total_revenue", total_revenue(prices, quantities)])
    writer.writerow(["average_price", average_price(prices)])
    writer.writerow(["best_product", best_product(products, prices, quantities)])
    writer.writerow(["total_items_sold", total_items_sold(quantities)])
