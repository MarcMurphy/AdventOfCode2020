def part1(data):
    i = 0
    while i < len(data):
        j = i + 1
        while j < len(data):
            if(data[i] + data[j] == 2020):
                return data[i] * data[j]
            j += 1
        i += 1
    return 0

def part2(data):
    i = 0
    while i < len(data):
        j = i + 1
        while j < len(data):
            k = j + 1
            while k < len(data):
                if(data[i] + data[j] + data[k]== 2020):
                    return data[i] * data[j] * data[k]
                k += 1
            j += 1
        i += 1
    return 0

data = open('Day_1/input.txt', 'r').read()

data = [int(i) for i in data.split()]

print(part1(data))
print(part2(data))