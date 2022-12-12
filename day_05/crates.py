def interpret_input():
    """

    :return: lists of crates and moving instructions
    """

    with open("input.txt") as f:
        lines = f.readlines()

    # split on the empty line
    split_point = lines.index("\n")

    boxes = lines[:split_point]
    instructions = lines[split_point+1:]

    for i, row in enumerate(boxes):
        boxes[i] = row.strip("\n")

    num_boxes = int(boxes[-1].split("   ")[-1])

    # each box column is three chars for a box and then a space between
    box_columns = {}
    for i in range(1, num_boxes+1):
        box_columns[i] = []

    max_line_length = (num_boxes * 3) + (num_boxes - 1)
    for i, row in enumerate(boxes):
        # lets pad them to the right so they are all the same length
        if len(row) < max_line_length:
            num_spaces_needed = max_line_length - len(row)
            boxes[i] = row+" "*num_spaces_needed

    backwards = boxes[:-1]
    backwards.reverse()
    # now do it backwards!
    for i, row in enumerate(backwards):
        box = 1
        for j in range(0, max_line_length, 4):
            if row[j:j+4].strip(" ") != "":
                box_columns[box].append(row[j:j+4].strip(" ").strip("[").strip("]"))
            box += 1

    # now handle the instructions
    formatted_instructions = []
    for instruction in instructions:
        no_words = instruction.strip("\n").replace("move ", "").replace(" from ", ",").replace(" to ", ",")
        formatted_instructions.append(no_words.split(","))

    return box_columns, formatted_instructions


def move_crates(box_columns, formatted_instructions):
    for num_boxes, from_col, to_col in formatted_instructions:
        for i in range(0, int(num_boxes)):
            moved = box_columns[int(from_col)].pop()
            box_columns[int(to_col)].append(moved)

    return box_columns


def move_crates_2(box_columns, formatted_instructions):
    for num_boxes, from_col, to_col in formatted_instructions:
        to_be_moved = box_columns[int(from_col)][len(box_columns[int(from_col)])-int(num_boxes):]
        del box_columns[int(from_col)][len(box_columns[int(from_col)])-int(num_boxes):]
        box_columns[int(to_col)].extend(to_be_moved)

    return box_columns

if __name__ == "__main__":
    boxes, instructions = interpret_input()
    #boxes_after = move_crates(boxes, instructions)
    boxes_after = move_crates_2(boxes, instructions)
    last_crate = ""
    for col, crates in boxes.items():
        last_crate = last_crate + crates[-1]
    print(last_crate)

    print("done")