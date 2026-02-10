import csv

def average_price(prices):
    return sum(prices) / len(prices)

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

def total_items_sold(quantities):
    return sum(quantities)
