import re

def part1(data):
    result = 0
    required = ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"]
    for dataset in data:
        dataset = dataset.strip('`n')
        if all(x in dataset for x in required):
            result += 1
    return result


def part2(data):
    result = 0
    required = ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"]
    allFields = ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:", "cid:"]
    for dataset in data:
        dataset = dataset.replace('\n', "").replace(' ', '')
        if all(x in dataset for x in required):
            try: 
                values = re.split('|'.join(allFields), dataset)
                values.pop(0)
                keys = re.findall('|'.join(allFields), dataset)
                subitems = dict(zip(keys, values))
                byrValid = 1920 <= (int)(subitems['byr:']) <= 2002
                iyrValid = 2010 <= (int)(subitems['iyr:']) <= 2020
                eyrValid = 2020 <= (int)(subitems['eyr:']) <= 2030
                hgtValid = (subitems["hgt:"].endswith("cm") and (150 <= (int)(subitems['hgt:'][:-2]) <= 193)) or (subitems["hgt:"].endswith("in") and (59 <= (int)(subitems['hgt:'][:-2]) <= 76)) 
                hclValid = re.match('#[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]', subitems["hcl:"]) and len(subitems["hcl:"]) == 7
                eclValid = subitems["ecl:"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                pidValid = re.match('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', subitems["pid:"]) and len(subitems["pid:"]) == 9

                if byrValid and iyrValid and eyrValid and hgtValid and hclValid and eclValid and pidValid:
                    result += 1
            except:
                pass
    return result

data = open('Day_4/input.txt', 'r').read().split('\n\n')

print(part1(data))
print(part2(data))