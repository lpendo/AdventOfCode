NumberStrings = (
    "DUMMY", 
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
)

import os
os.chdir(os.path.dirname(__file__))

with open("input", "r", encoding="utf-8") as fstream:
    Sum_CVals = 0
    for line in fstream:
        
        IsSet_First = False
        IsSet_Number = False

        for i,x in enumerate(line):
            if x.isdigit():
                z = int(x)
                IsSet_Number = True
            else:
                for n in range(1,10):
                    NS = NumberStrings[n]
                    if ( line[i:i+len(NS)] == NS ):
                        z = n
                        IsSet_Number = True
            if IsSet_Number and not IsSet_First:
                FirstDigit = z
                Sum_CVals += 10*z 
                IsSet_First = True
            #     print(line, "   ", FirstDigit, " ", z)
            # else:
            #     print("       ", FirstDigit, " ", z)
        Sum_CVals += z

    print(Sum_CVals)