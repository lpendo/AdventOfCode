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
    for m in compile(r"A").finditer(line)
]




# Digestion ------------------------------

from collections import Counter

# https://docs.python.org/3/library/collections.html#collections.Counter

ans = 0
NumLines = len(InBuff)
for r0,c0 in candidates:
    NumCols = len(InBuff[r0])

    if ( r0 == 0 ) : continue
    if ( r0 == NumLines-1 ) : continue

    if ( c0 == 0 ) : continue
    if ( c0 == NumCols-1 ) : continue

    my_counts = Counter( (
        InBuff[r0-1][c0-1],
        InBuff[r0+1][c0+1],
        InBuff[r0-1][c0+1],
        InBuff[r0+1][c0-1]
    ) )
    
    if ( my_counts['M'] == 2 and my_counts['S'] == 2 ) :
        if ( 
            ( InBuff[r0-1][c0-1] != InBuff[r0+1][c0+1] )
            and 
            ( InBuff[r0+1][c0-1] != InBuff[r0-1][c0+1] )
        ) : ans += 1

print(ans)