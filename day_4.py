from typing import *

with open('inputs/4.txt') as f:
    data = f.read().splitlines()
    ans = []
    for i, line in enumerate(data):
        matches = 0
        winning, have = line.split("|")
        winning = winning[winning.index(":") + 2:].split()
        have = have.split()
        for num in have:
            if num in winning:
                matches += 1
        if matches != 0:
            ans.append(2**(matches - 1))
    print(sum(ans))