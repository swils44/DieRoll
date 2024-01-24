from Dice import rolldice as rd
from Die import prob1k as prob
from Dice import calculate_probabilities as calc
import Dice

def main(n):
    """
    Calls calculate_probabilities function and rollDice(N) 1000 times and outputs the score and probability of different
    rolls
    :param n: number of dice rolled
    :return: score and probability
    """
    probabilities = calc(n, num_trials=1000)
    for score, probability in probabilities.items():
        print(f"Probability of rolling a {score}:  {probability:.3f}")



N = int(input("Number of dice(n) to roll: "))
main(N)