import matplotlib.pyplot as plt

soil_samples = [
    .74, .32, 1.66, 3.59, 4.55, 6.47, 1.90, 
    2.69, .75, 9.99, 1.77, 2.41, 1.96, .70,
    2.42, .54, 3.36, .37,1.09, 8.32, 4.06,
    .76, 2.03, 5.70, 12.48
]

# create histogram
plt.figure(figsize=(10, 6))
plt.hist(soil_samples, bins=10)
plt.title('Histogram of Soil Samples')
plt.xlabel('Soil Sample (picocuries per gram)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()