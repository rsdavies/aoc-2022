
import numpy as np

# score matrix
##  A  B  C
#X
#Y
#Z


def score_strategy_part1(strategy):
    """
    A = X = Rock
    B = Y = Paper
    C = Z = Scissors
    """

    score_matrix = [[3, 0, 6],
                    [6, 3, 0],
                    [0, 6, 3]]

    score_matrix = np.asarray(score_matrix)

    score_mapper = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    play_scorer = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    score = 0
    for play in strategy:
        them, me = play.strip('\n').split()
        # print("score1:")
        # print(score_matrix[score_mapper[me], score_mapper[them]])
        # print("score2:")
        # print(play_scorer[me])
        score += (score_matrix[score_mapper[me], score_mapper[them]] + play_scorer[me])

    return score


def score_strategy_part2(strategy):
    """
    A = rock = 1
    B = paper = 2
    C = scissors = 3

    X = lose = 0
    Y = draw = 3
    Z = win = 6
    """
    ##  A  B  C
    # X
    # Y
    # Z

    score_matrix = [[0+3, 0+1, 0+2],
                    [3+1, 3+2, 3+3],
                    [6+2, 6+3, 6+1]]
    score_matrix = np.asarray(score_matrix)
    score_mapper = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    score = 0

    for play in strategy:
        them, me = play.strip('\n').split()

        score += score_matrix[score_mapper[me], score_mapper[them]]

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        strategy = f.readlines()
    score = score_strategy_part1(strategy)
    print(score)
    score2 = score_strategy_part2(strategy)
    print(score2)