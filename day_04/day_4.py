def part_1():

    with open("input.txt") as f:
        assignments = f.readlines()

    needs_reassignment = 0

    for assignment in assignments:
        a, b = assignment.strip("\n").split(",")
        a_start, a_end = a.split("-")
        b_start, b_end = b.split("-")

        all_a = list(range(int(a_start), int(a_end) + 1))

        all_b = list(range(int(b_start), int(b_end) + 1))

        if set(all_a).issubset(all_b) or set(all_b).issubset(all_a):
            needs_reassignment += 1

    return needs_reassignment


def part_2():

    with open("input.txt") as f:
        assignments = f.readlines()

    needs_reassignment = 0

    for assignment in assignments:
        a, b = assignment.strip("\n").split(",")
        a_start, a_end = a.split("-")
        b_start, b_end = b.split("-")

        all_a = list(range(int(a_start), int(a_end) + 1))

        all_b = list(range(int(b_start), int(b_end) + 1))

        if set(all_a).intersection(all_b):
            needs_reassignment += 1

    return needs_reassignment


if __name__ == "__main__":
    result = part_1()
    print(result)

    result = part_2()
    print(result)