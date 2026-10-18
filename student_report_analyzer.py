import numpy as np
names = np.loadtxt("data.txt", delimiter = ",", skiprows = 1, usecols = 0, dtype=str)
grades = np.loadtxt("data.txt", delimiter=",",skiprows=1, usecols = (1,2,3,4))
averages = grades.mean(axis=1)
print("Student failed: ", names[averages < 75] )
