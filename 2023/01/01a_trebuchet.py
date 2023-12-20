import os
os.chdir(os.path.dirname(__file__))

with open("input", "r", encoding="utf-8") as fstream:
    Sum_CVals = 0
    for line in fstream:

        IsSet_First = False
        FirstDigit = 0
        SecondDigit = 0
        
        for x in line:
            if x.isdigit():
                if not IsSet_First:
                    FirstDigit = int(x)
                    IsSet_First = True
                SecondDigit = int(x)
        Sum_CVals += 10*FirstDigit + SecondDigit
        
    print(Sum_CVals)