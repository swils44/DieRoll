from Die import rollFairDie as rfd
from Die import prob1k
from Die import prob10k
from Die import rollUnfairDie as ufd
def main():

    for i in range(1000):
        rfd()
    prob1k()

def main2():
    for i in range(10000):
        rfd()
    prob10k()

def main3():
    for i in range(10000):
        ufd()
    prob10k()


main()
main2()
main3()
