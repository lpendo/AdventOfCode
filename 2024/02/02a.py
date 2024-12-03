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

InBuff = [s.split() for s in InBuff.split('\n')]
InBuff = [ [ int(xs) for xs in s ] for s in InBuff if len(s) != 0 ]




# Preparing ------------------------------

from itertools import pairwise

# https://docs.python.org/3/library/stdtypes.html#str
# https://docs.python.org/3/library/itertools.html#itertools.pairwise

Prepped = [ sorted([ a-b for a,b in pairwise(xs) ]) for xs in InBuff ]




# Digestion ------------------------------

# https://docs.python.org/3/tutorial/controlflow.html

ans = 0 
for xs in Prepped:
    print('ans: ', ans)
    if xs[0]*xs[-1] < 1 :
        continue

    for x in xs :
        if abs(x) < 1 or abs(x) > 3 :
            break
    else :
        ans += 1


print(ans)

