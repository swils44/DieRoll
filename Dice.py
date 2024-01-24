from Die import rollUnfairDie as ufd
from Die import rollFairDie as rfd

x =0

def rolldice(N):
    """
    Simulates rolling N dice and return the sum of the outcomes
    :param N:Number of dice rolled
    :return:The Sum
    """

    return sum([rfd() for _ in range(N)])



def calculate_probabilities(N, num_trials=1000):
    """Calculate probabilities for each possible score when rolling N dice."""
    outcomes = [rolldice(N) for _ in range(num_trials)]
    min_score = N
    max_score = N * 6
    probabilities = {score: outcomes.count(score) / num_trials for score in range(min_score, max_score + 1)}
    return probabilities
