import os
os.chdir(os.path.dirname(__file__))


def ProcessLine(Line0,Line1,Line2):
    from re import sub

    Idx0 = 0
    Idx1 = 0
    n0 = 0
    n1 = 0
    Sum = 0
    while n0 < len(Line1):
        c = Line1[n0]
        s = ''
        if c.isnumeric():
            Idx0 = n0
            for n1,c in enumerate(Line1[n0+1:]): 
                if not c.isnumeric():
                    Idx1 = n0 + n1
                    break
            s = Line0[max(0,Idx0-1):min(Idx1+2,len(Line0))]
            s += Line1[max(0,Idx0-1):min(Idx1+2,len(Line1))]
            s += Line2[max(0,Idx0-1):min(Idx1+2,len(Line2))]
            s = sub(r'[\n.0-9]','',s)

            if s != '':
                x = int(Line1[Idx0:Idx1+1])
                Sum += x
            
            n0 = Idx1
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