import random
import math

prob1 = 0
prob2 = 0
prob3 = 0
prob4 = 0
prob5 = 0
prob6 = 0
total = 1000
total2 = 10000
def rollFairDie():
    """
        sets x to a random integer between 0.0 and 1.0 divides that by 6 and checks if it is less
        than or equal to 1-6 and returns the value that matches
    :return:
    """
   # x = math.ceil((random.random()) * 6) sets x to a random int to from 0.0 to 1.0 multiplies it by 6 and rounds up.
   # print(x)

    global prob1
    global prob2
    global prob3
    global prob4
    global prob5
    global prob6


    x = random.random()
    if (x  <= 1.0/6):
        prob1 += 1
        return 1
    elif(x  <= 2.0/6):
        prob2 += 1
        return 2
    elif (x <= 3.0/6):
        prob3 += 1
        return 3
    elif (x<=4.0/6):
        prob4 += 1
        return 4
    elif (x <= 5.0/6):
        prob5 += 1
        return 5
    elif (x<=6.0/6):
        prob6 += 1
        return 6
def prob1k():
    """
    Calculates the total probability of rolling each number on a die
    Uses the global variable prob1-prob6 which count each time a number on a die is rolled
    then divides that by the total number of rolls 1000
    :return:
    """
    global total
    global prob1
    global prob2
    global prob3
    global prob4
    global prob5
    global prob6
    prob1 = prob1 / total
    prob2 = prob2 / total
    prob3 = prob3 / total
    prob4 = prob4 / total
    prob5 = prob5 / total
    prob6 = prob6 / total
    print(f"After rolling the die {total} times:")
    print(f"Probability of rolling a 1: {prob1}")
    print(f"Probability of rolling a 2: {prob2}")
    print(f"Probability of rolling a 3: {prob3}")
    print(f"Probability of rolling a 4: {prob4}")
    print(f"Probability of rolling a 5: {prob5}")
    print(f"Probability of rolling a 6: {prob6}")

def prob10k():
    """
        Calculates the total probability of rolling each number on a die
        Uses the global variable prob1-prob6 which count each time a number on a die is rolled
        then divides that by the total number of rolls 10,000
        :return:
        """
    global total2
    global prob1
    global prob2
    global prob3
    global prob4
    global prob5
    global prob6
    prob1 = prob1 / total2
    prob2 = prob2 / total2
    prob3 = prob3 / total2
    prob4 = prob4 / total2
    prob5 = prob5 / total2
    prob6 = prob6 / total2
    print(f"After rolling the die {total2} times:")
    print(f"Probability of rolling a 1: {prob1}")
    print(f"Probability of rolling a 2: {prob2}")
    print(f"Probability of rolling a 3: {prob3}")
    print(f"Probability of rolling a 4: {prob4}")
    print(f"Probability of rolling a 5: {prob5}")
    print(f"Probability of rolling a 6: {prob6}")

def rollUnfairDie():
    """
           sets x to a random integer between 0.0 and 1.0 divides that by 6 for 2-6 and is divided by 5 for 1 so that 1
           has a higher chance of being rolled
       :return:
       """


    global prob1
    global prob2
    global prob3
    global prob4
    global prob5
    global prob6

    x = random.random()
    if (x <= 1.0 / 5):
        prob1 += 1
        return 1
    elif (x <= 2.0 / 6):
        prob2 += 1
        return 2
    elif (x <= 3.0 / 6):
        prob3 += 1
        return 3
    elif (x <= 4.0 / 6):
        prob4 += 1
        return 4
    elif (x <= 5.0 / 6):
        prob5 += 1
        return 5
    elif (x <= 6.0 / 6):
        prob6 += 1
        return 6
