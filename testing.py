import random
import math
from Die import rollFairDie as rfd
def rollFairDie():
    #x = random.random()
    #x = random.random()
    # x = x * 6
    #x = math.ceil(x)
    for i in range(100):
        x = math.ceil((random.random()) * 6) #sets x to a random int to from 0.0 to 1.0 multiplies it by 6 and rounds up.
        print(f"this is x: {x}")


rollFairDie()
def rolldice():
    """

    :return:
    """
    for i in range(1000):
        print(f"probability of rolling a {i}: some")
rolldice()


