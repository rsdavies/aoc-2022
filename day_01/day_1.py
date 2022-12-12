# todo 
# 1. read the input
# 2. sum each block of input
# 3. work out the highest calories

with open("input.txt") as f:
    input = f.readlines()

elves = [0]

elf_num = 0   

for line in input: 
    stripped = line.strip('\n')

    if stripped == "":
        elf_num += 1
        elves.append(0)
    else:
       #  elves[elf_num].append(int(stripped))
        elves[elf_num] += int(stripped)

elves.sort()
print(elves)
print(max(elves))

print(elves[-3:])

print(sum(elves[-3:]))
