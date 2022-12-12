def part_1():
    # lowercase priorities = ord(letter) - 96
    # uppercase priorities = ord(letter) - 38

    with open("input.txt") as f:
        bag_contents = f.readlines()

    priority = 0

    for bag in bag_contents:
        bag = bag.strip("\n")

        size_pocket = int(len(bag)/2)
        pocket1 = bag[:size_pocket]
        pocket2 = bag[size_pocket:]
        in_both = list(set(pocket2).intersection(pocket1))[0]

        if in_both.isupper():
            priority += (ord(in_both) - 38)
        else:
            priority += (ord(in_both) -96)

    return priority


def part2():

    with open("input.txt") as f:
        bag_contents = f.readlines()

    priority = 0

    num_teams = int(len(bag_contents)/3)

    for team in range(0, num_teams):
        bag1 = bag_contents[0 + 3 * team]
        bag2 = bag_contents[1 + 3 * team]
        bag3 = bag_contents[2 + 3 * team]

        badge = list(set(bag1.strip("\n")).intersection(bag2.strip("\n"), bag3.strip("\n")))[0]

        if badge.isupper():
            priority += (ord(badge) - 38)
        else:
            priority += (ord(badge) - 96)

    return priority


if __name__ == "__main__":
    result = part_1()
    print(result)

    result2 = part2()
    print(result2)