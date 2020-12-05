import re
import math

def part1(data):
    highest = 0
    for dataset in data:
        rowMin = 0
        rowMax = 127
        columnMin = 0
        columnMax = 7
        for char in dataset:
            if char == 'B':
                rowMin += math.ceil((rowMax - rowMin) / 2)
            elif char == 'F':
                rowMax -= math.ceil((rowMax - rowMin) / 2)
            elif char == 'R':
                columnMin += math.ceil((columnMax - columnMin) / 2)
            elif char == 'L':
                columnMax -= math.ceil((columnMax - columnMin) / 2)

        if rowMin * 8 + columnMin > highest:
            highest = rowMin * 8 + columnMin

    return highest

def part2(data):
    seatIds = []
    for dataset in data:
        rowMin = 0
        rowMax = 127
        columnMin = 0
        columnMax = 7
        for char in dataset:
            if char == 'B':
                rowMin += math.ceil((rowMax - rowMin) / 2)
            elif char == 'F':
                rowMax -= math.ceil((rowMax - rowMin) / 2)
            elif char == 'R':
                columnMin += math.ceil((columnMax - columnMin) / 2)
            elif char == 'L':
                columnMax -= math.ceil((columnMax - columnMin) / 2)
        seatIds.append(rowMin * 8 + columnMin)
    seatIds.sort()
    seatIds = list(set(seatIds))
    
    previous = seatIds[0] - 1
    for seat in seatIds:
        if previous + 1 != seat:
            return previous + 1
        previous = seat

data = open('Day_5/input.txt', 'r').read().splitlines()

print(part1(data))
print(part2(data))