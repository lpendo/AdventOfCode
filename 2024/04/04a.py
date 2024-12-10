# import urllib.request as req Target =
# 'https://adventofcode.com/2024/day/1/input'
# # From https://docs.python.org/3/howto/urllib2.html
# with req.urlopen(Target) as response: Input = response.open()
# 
# Above will require more work with the AoC API to deal with authentication.



# Gathering ------------------------------

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files


# using dl'd file from AoC website
full = 'input.txt'
test0 = 'test0.txt'

with open(full, encoding="utf-8") as file:
    InBuff = file.read()
InBuff = InBuff.split('\n')
if len(InBuff[-1]) == 0 : InBuff = InBuff[:-1]


# Preparing ------------------------------

from re import compile

# https://docs.python.org/3/howto/regex.html


candidates = [ 
    ( n,m.start() )
    for n,line in enumerate(InBuff)
    for m in compile(r"X").finditer(line)
    
]




# Digestion ------------------------------

from itertools import product

# https://docs.python.org/3/library/itertools.html#itertools.product


ans = 0
NumLines = len(InBuff)
for r0,c0 in candidates:
    NumCols = len(InBuff[r0])

    # print()
    # print(r0,",",c0)
    for dr, dc in product( (-1,0,+1), repeat=2 ):
        if dr == 0 and dc == 0 : continue
        if ( r0+3*dr < 0 ) or ( c0+3*dc < 0 ) : continue
        if ( r0+3*dr >= NumLines ) or ( c0+3*dc >= NumCols ) : continue

        # print("D:    ",dr,",",dc)

        if (InBuff[r0+dr][c0+dc] != "M") : continue
        if (InBuff[r0+2*dr][c0+2*dc] != "A") : continue
        if (InBuff[r0+3*dr][c0+3*dc] != "S") : continue

        # print("Whee!")
        ans += 1

print(ans)