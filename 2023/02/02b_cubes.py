import os
os.chdir(os.path.dirname(__file__))

from math import prod

with open("input", "r", encoding="utf-8") as fstream:
    PowerSum = 0
    for Game in fstream:
        GameId = int( Game.split(":")[0][5:] )
        GameDat = Game.split(":")[1]
        Dt = { "red":0, "green":0, "blue":0 }
        for Trial in GameDat.split(";"):
            for Cat in Trial.split(","):
                num,color = Cat.split()
                num = int(num)
                if num > Dt[color]:
                    Dt[color] = num
        PowerSum += prod(Dt.values())
    print(PowerSum)