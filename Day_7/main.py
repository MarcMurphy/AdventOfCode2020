import re


def part1(dataset):
    targets = ['shiny gold']
    suitableBags = []

    while targets:
        for data in dataset:
            if (' ' + targets[0]) in data:
                targets.append(' '.join(data.split()[:2]))
                suitableBags.append(' '.join(data.split()[:2]))
        del targets[0]

    return len(set(suitableBags))


def part2(dataset):
    targets = [(1, 'shiny gold bags contain ')]
    result = 1

    while targets:
        for data in dataset:
            if (targets[0][1]) in data:
                data = data.replace(targets[0][1], '')

                for match in data.split(','):
                    words = match.split()
                    targets.append(tuple([int(words[0]), ' '.join(words[1:4]) + 's contains']))
        del targets[0]

    return result


data = open('Day_7/input.txt', 'r').read().splitlines()

# print(part1(data))
print(part2(data))
