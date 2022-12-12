from day_2 import score_strategy_part1


def test_score_strategy_part_1():
    test_input = ["A Y", "B X", "C Z"]
    result = score_strategy_part1(test_input)
    assert result == 15
