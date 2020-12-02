import re

def part1(data):
    result = 0
    for row in data:
        arr = re.findall('\w+', row)
        charCount = arr[3].count(arr[2])
        if charCount >= (int)(arr[0]) and charCount <= (int)(arr[1]):
            result += 1
    return result


def part2(data):
    result = 0
    for row in data:
        arr = re.findall('\w+', row)
        indexOne = (int)(arr[0]) - 1
        indexTwo = (int)(arr[1]) - 1
        if (arr[3][indexOne] == arr[2]) != (arr[3][indexTwo] == arr[2]):
            result += 1
    return result

data = open('Day_2/input.txt', 'r').read().splitlines()

print(part1(data))
print(part2(data))