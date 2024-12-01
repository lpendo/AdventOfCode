import os
os.chdir(os.path.dirname(__file__))

from re import sub
from collections import defaultdict

Cards = []

with open("input", "r", encoding="utf-8") as fstream:
    Sum = 0
    for Line in fstream:
        WinningNumbersRaw,GivenNumbersStr = Line.split('|')
        GameIdRaw,WinningNumbersStr = WinningNumbersRaw.split(':')        

        GameId = int(sub(r'[ a-zA-Z]','',GameIdRaw))

        GivenNumbers = { int(s) for s in GivenNumbersStr.split() }
        WinningNumbers = { int(s) for s in WinningNumbersStr.split() }

        n = 0
        for x in GivenNumbers:
            if x in WinningNumbers:
                n += 1

        for m in range(n+1):
            m1 = GameId-1+m
            if m1 == len(Cards):
                Cards.append(1)
            else:
                if m == 0:
                    Cards[GameId-1] += 1
                else:
                    Cards[m1] += Cards[GameId-1]

        # Sum += ( 0 if n == 0 else 2**(n-1) )
    Sum = sum(Cards)

    print(Sum)