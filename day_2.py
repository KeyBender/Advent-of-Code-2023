""" What is the sum of the IDs of those games? """
""" only 12 red cubes, 13 green cubes, and 14 blue cubes """
from typing import *


def validGame(game: List[str]):
    """ 1. split elements by spaces ['number of blocks', 'color of blocks']
        2. add up blocks by color, store in dict
        3. if any of the colors pass the limit, return false, otherwise true
        """

    for block in game:
        colorBlocks = {
            'red': 0,
            'green': 0,
            'blue' : 0
        } 
        n, color = block.strip().split()
        colorBlocks[color.strip()] += int(n)
        if colorBlocks['red'] > 12 or colorBlocks['green'] > 13 or colorBlocks['blue'] > 14:
            return False
    return True

with open('inputs/2.txt') as f:
    data = f.read().splitlines()

    ans = 0

    #print(data)

    for i, line in enumerate(data):
        for game in line[line.index(':')+2:].split(';'):
            if validGame(game.strip().split(',')):
                
                ans += i+1
            

print(ans) # Too high?? where is this going wrong? 