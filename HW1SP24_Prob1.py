

from Die import rollFairDie as rfd
from Die import prob1k
from Die import prob10k
from Die import rollUnfairDie as ufd

def main():
    """
    Calls function rollFairDie 1000 times and then calls the prob1k function to get the probability of rolling
    each number
    :return: The value from rollFairDie
    """
    print("-----Roll 1000 Fair Dice-----")
    for i in range(1000):
         rfd()
    prob1k()
    print()

def main2():
    """
    calls rollFairDie function 10,000 times and then calls prob10k function to calculate the probability of rolling a
    1-6 after rolling a die 10,000 times.
    :return:probabilities of rolling a 1-6
    """
    print("-----Roll 10,000 Fair Dice-----")
    for i in range(10000):
        rfd()
    prob10k()
    print()
def main3():
    """
        calls rollUnfairDie function 10,000 times and then calls prob10k function to calculate the probability of
        rolling a 1-6 after rolling a die 10,000 times with the probability of rolling a 1 being 0.2.
        :return:probabilities of rolling a 1-6
        """
    print("-----Roll 10,000 Weighted Dice-----")
    for i in range(10000):
        ufd()
    prob10k()
    print()
# this is a comment

main()
main2()
main3()
