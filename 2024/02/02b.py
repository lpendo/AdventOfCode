# import urllib.request as req Target =
# 'https://adventofcode.com/2024/day/1/input'
# # From https://docs.python.org/3/howto/urllib2.html
# with req.urlopen(Target) as response: Input = response.open()
# 
# Above will require more work with the AoC API to deal with authentication.


# Gathering ------------------------------

from itertools import combinations, chain

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/stdtypes.html#str
# https://docs.python.org/3/library/itertools.html#itertools.combinations
# https://docs.python.org/3/library/itertools.html#itertools.chain

# using dl'd file from AoC website
full = 'input.txt'
test0 = 'test0.txt'

with open(full, encoding="utf-8") as file:
    InBuff = file.read()

InBuff = [s.split() for s in InBuff.split('\n')]
InBuff = [
    [
        [ int(xs) for xs in ss ]
        for ss in chain( (s,), combinations( s, len(s)-1 ) )
    ] 
    for s in InBuff if len(s) != 0 
]



# Preparing ------------------------------

from itertools import pairwise

# https://docs.python.org/3/library/itertools.html#itertools.pairwise

Prepped = [
    [ 
        sorted([ a-b for a,b in pairwise(ss) ])
        for ss in s
    ]
    for s in InBuff
]




# Digestion ------------------------------

# https://docs.python.org/3/tutorial/controlflow.html

ans = 0 
for s in Prepped:
    # print("------------------------------------------------")
    for ss in s:

        try:
            NotStrictlyMonotonic = ss[0]*ss[-1] < 1
        except IndexError:
            # Sequence only has one element.
            # This is "strictly monotonic" for our purposes
            NotStrictlyMonotonic = False

        if NotStrictlyMonotonic : continue

        for x in ss :
            if abs(x) < 1 or abs(x) > 3 : break
        else :
            ans += 1
            break


print(ans)