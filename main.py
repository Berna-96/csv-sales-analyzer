import csv

def total_revenue(prices, quantities):
    total = 0
    for price, quantity in zip(prices, quantities):
        total += price * quantity
    return total


def best_product(products, prices, quantities):
    revenues = []
    for price, quantity in zip(prices, quantities):
        revenues.append(price * quantity)

    max_index = revenues.index(max(revenues))
    return products[max_index]


def average_price(prices):
    return sum(prices) / len(prices)

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
