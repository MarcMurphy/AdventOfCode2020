import re

def part1(data):
    x = 0
    y = 0
    result = 0
    while y < len(data):
        if data[y][x] == '#':
            result += 1
        x = (x + 3) % len(data[y])
        y += 1
    return result


def part2(data, right, down):
    x = 0
    y = 0
    result = 0
    while y < len(data):
        if data[y][x] == '#':
            result += 1
        x = (x + right) % len(data[y])
        y += down
    return result

data = open('Day_3/input.txt', 'r').read().splitlines()

print(part1(data))
print(part2(data, 1, 1) * part2(data,3,1) * part2(data,5,1) * part2(data,7,1) * part2(data,1,2))