daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# memory efficient operation
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)