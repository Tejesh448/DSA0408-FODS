
import numpy as np
fuel_efficiency = np.array([25, 30, 35, 40, 45])
average_efficiency = np.mean(fuel_efficiency)
car1 = fuel_efficiency[0]
car2 = fuel_efficiency[4]
percentage_improvement = ((car2 - car1) / car1) * 100
print("Average fuel efficiency:", average_efficiency, "MPG")
print("Car 1 fuel efficiency:", car1, "MPG")
print("Car 2 fuel efficiency:", car2, "MPG")
print("Percentage improvement:", percentage_improvement, "%")
