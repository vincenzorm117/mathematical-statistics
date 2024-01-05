import matplotlib.pyplot as plt

stock_trade_percentages = [
    11.88, 6.27, 5.49, 4.81, 4.40, 3.78, 3.44, 3.11, 2.88, 2.68,
    7.99, 6.07, 7.15, 5.98, 7.13, 5.91, 5.26, 4.79, 4.05, 3.69,
    5.07, 4.55, 3.94, 3.62, 4.94, 4.43, 3.93, 3.48, 3.36, 3.03,
    2.74, 2.63, 3.26, 2.99, 2.74, 2.62, 3.20, 2.89, 2.69, 2.61
]

# Percentage of percentage greater than 4%
greater_than_4_percent = len([1 for s in stock_trade_percentages if s > 4.0])
percentage = round(greater_than_4_percent/len(stock_trade_percentages), 2)
print(f"Percentage of percentage trades greater than 4%: {percentage}")


# create histogram
plt.figure(figsize=(10,6))
plt.hist(stock_trade_percentages, bins=15)
plt.xlabel("Percentage Ranks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()