
import numpy as np
house_data = np.array([
    [3, 1200, 200000],
    [5, 2000, 350000],
    [4, 1500, 250000],
    [6, 2500, 450000],
    [5, 2200, 400000]
])
filtered_houses = house_data[house_data[:, 0] > 4]
average_price = np.mean(filtered_houses[:, 2])
print("Average sale price of houses with more than 4 bedrooms:",
      average_price)

