# import urllib.request as req Target =
# 'https://adventofcode.com/2024/day/1/input'
# # From https://docs.python.org/3/howto/urllib2.html
# with req.urlopen(Target) as response: Input = response.open()
# 
# Above will require more work with the AoC API to deal with authentication.



# Gathering ------------------------------

from re import compile

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/reference/compound_stmts.html#while


# using dl'd file from AoC website
full = 'input.txt'
test0 = 'test0.txt'
test1 = 'test1.txt'

with open(full, encoding="utf-8") as file:
    InBuff = file.read()


# InBuff = InBuff[:2000]


do = ( 0, ) + tuple(
    m.start()
    for m in compile(r"do\(\)").finditer(InBuff)
)
i0 = iter(do)

donot = tuple(
    m.end()
    for m in compile(r"don't\(\)").finditer(InBuff)
)
i1 = iter(donot)


n0 = next(i0)
try:    
    n1 = next(i1)
    slices = [ slice(n0,n1) ]

    while n0 < n1:
        try:
            n0 = next(i0)
        except StopIteration:
            break

    for n1 in i1:
        if n1 > n0:
            slices.append( slice(n0,n1 ) )
            while n0 < n1:
                try:
                    n0 = next(i0)
                except StopIteration:
                    break
        else:
            continue

    if n1 < n0:
        slices.append( slice(n0,None) )        
except IndexError:
    pass


InBuff = ''.join( InBuff[sl] for sl in slices )



# Preparing ------------------------------


InData = [
        tuple( int(s) for s in m.group()[4:-1].split(',') )
        for m in compile(r"mul\(\d+,\d+\)").finditer(InBuff)
]


# Digestion ------------------------------

from itertools import starmap
from operator import mul

# https://docs.python.org/3/library/itertools.html#itertools.starmap
# https://docs.python.org/3/library/operator.html


ans = sum(starmap(mul,InData))
print(ans)