import matplotlib.pyplot as plt

# Data of average wind speeds in miles per hour
wind_speeds = [
    8.9, 12.4, 7.1, 11.8, 9.1, 10.9, 8.8, 12.7, 10.2, 10.3,
    8.6, 11.3, 10.7, 7.6, 10.3, 9.6, 8.4, 7.8, 7.7, 10.6,
    9.2, 8.8, 9.1, 9.2, 8.2, 7.8, 11.5, 9.3, 5.7, 
    10.5, 10.5, 8.3, 8.8, 9.5, 6.2, 7.0, 9.0, 8.7, 7.9, 
    8.8, 9.6, 8.9, 8.8, 9.4
]

# Get percentage of wind speeds greater than 10.3 mph
greater_than_10_3 = len([speed for speed in wind_speeds if speed > 10.3])
percentage = round(greater_than_10_3/len(wind_speeds), 2)
print(f"Percentage of wind speeds greater than 10.3 mph: {percentage}")

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(wind_speeds, bins=15, color='skyblue', edgecolor='black')
plt.title('Histogram of Average Wind Speeds')
plt.xlabel('Wind Speed (mph)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
