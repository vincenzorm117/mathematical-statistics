import matplotlib.pyplot as plt

aluminum_oxide_portions = [
    14.4, 11.6, 13.8, 11.1, 14.6, 13.4,
    11.5, 12.4, 13.8, 13.1, 10.9, 12.7,
    10.1, 12.5, 11.8, 11.6, 18.3, 15.8,
    18.0, 18.0, 20.8, 17.7, 18.3, 16.7,
    14.8, 19.1
]

# create histogram
plt.figure(figsize=(10,6))
plt.hist(aluminum_oxide_portions, bins=12)
plt.xlabel("Aluminum Oxide Portions")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()