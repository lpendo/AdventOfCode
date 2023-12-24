import os
os.chdir(os.path.dirname(__file__))

def NumberCapture(n0,Line):
    if Line == '':
        return []

    n1 = n0 - 1
    while n1 >= 0:
        if not Line[n1].isnumeric():
            n1 += 1
            break
        n1 -= 1
    n1 = max(0,n1)

    n2 = n0 + 1
    while n2 < len(Line):
        if not Line[n2].isnumeric():
            break
        n2 += 1
    
    if Line[n0].isnumeric():
        return [ int(Line[n1:n2]), ]
    else:
        res = []
        if Line[n1:n0]:
            res.append(int(Line[n1:n0]))
        if Line[n0+1:n2]:
            res.append(int(Line[n0+1:n2]))
    
    return res


def ProcessLine(Line0,Line1,Line2):
    n0 = 0
    Sum = 0
    while n0 < len(Line1):
        c = Line1[n0]
        if c == '*':
            Nums = NumberCapture(n0,Line0)
            Nums += NumberCapture(n0,Line1)
            Nums += NumberCapture(n0,Line2)

            if len(Nums) == 2:
                Ratio = Nums[0] * Nums[1]
                Sum += Ratio
        n0 += 1
    return Sum


with open("input", "r", encoding="utf-8") as fstream:
    Line0 = ''
    Line1 = fstream.readline()
    
    Line2 = fstream.readline()
    Sum = ProcessLine(Line0,Line1,Line2)
    Line0 = Line1
    Line1 = Line2
    
    for Line2 in fstream:
        Sum += ProcessLine(Line0,Line1,Line2)
        Line0 = Line1
        Line1 = Line2

    Line2 = ''
    Sum += ProcessLine(Line0,Line1,Line2)

    print(Sum)