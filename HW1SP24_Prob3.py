import math
import random
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm
from math import sqrt
#x =[]
#for i in range(1000):
   # x.append(random.normalvariate())
mean = float(input("Enter the wanted mean: "))
std_dev = float(input("Enter the wanted Standard Deviation: "))
x = [random.normalvariate(mean, std_dev) for _ in range(1000)]

print(x)

mu = statistics.mean(x)
std = statistics.stdev(x)

print(f"The Array size is {len(x)}")
print(f"The calculated mean is {mu}")
print(f"The calculated standard deviation {std}")

plt.hist(x, bins=100)
plt.show()