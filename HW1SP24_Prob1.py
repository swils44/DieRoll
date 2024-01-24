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

    :return:
    """
    print("-----Roll 10,000 Fair Dice-----")
    for i in range(10000):
        rfd()
    prob10k()
    print()
def main3():
    print("-----Roll 10,000 Weighted Dice-----")
    for i in range(10000):
        ufd()
    prob10k()
    print()

main()
main2()
main3()
