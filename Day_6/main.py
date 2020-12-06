from collections import Counter

def part1(data):
    result = 0
    for dataset in data:
        dataset = dataset.replace('\n', '')
        result += len(set(dataset))
    return result

def part2(data):
    result = 0
    for dataset in data:
        people = dataset.count('\n') + 1
        dataset = dataset.replace('\n', '')
        occurences = Counter(dataset)
        for count in occurences.values():
            if count == people:
                result += 1
    return result

data = open('Day_6/input.txt', 'r').read().split('\n\n')

print(part1(data))
print(part2(data))