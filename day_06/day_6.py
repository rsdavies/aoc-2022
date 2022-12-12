import itertools
import collections


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def identify_packet(data):
    # a packet is four different characters
    i = 4
    for four_chars in sliding_window(data, 4):
        if len(set(four_chars)) == 4:
            return i
        else:
            i = i+1

    return i


def identify_message(data):
    i = 14
    for fourteen_chars in sliding_window(data, 14):
        if len(set(fourteen_chars)) == 14:
            return i
        else:
            i = i+1

    return i


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readline()

    data.strip("\n")
    data = list(data)
    num = identify_packet(data)
    print(num)

    num2 = identify_message(data)
    print(num2)