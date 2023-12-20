Ct = { "red":12, "green":13, "blue":14 }
TotalCubes = sum(Ct.values())


import os
os.chdir(os.path.dirname(__file__))
with open("input", "r", encoding="utf-8") as fstream:
    IdSum = 0
    for Game in fstream:
        GameId = int( Game.split(":")[0][5:] )
        GameDat = Game.split(":")[1]
        Possible = True
        for Trial in GameDat.split(";"):
            for Cat in Trial.split(","):
                num,color = Cat.split()
                num = int(num)
                if num > Ct[color]:
                    Possible = False
                    break
            if not Possible:
                break
        if Possible:
            IdSum += GameId
    print(IdSum)