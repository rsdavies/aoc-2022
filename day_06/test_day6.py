from day_6 import identify_packet
import pytest

@pytest.mark.parametrize("data, expected", [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
                                          ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
                                          ("nppdvjthqldpwncqszvftbrmjlhg", 6),
                                          ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
                                          ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)])
def test_identify_packet(data, expected):
    actual = identify_packet(data)

    assert actual == expected