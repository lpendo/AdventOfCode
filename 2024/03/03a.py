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
test = 'test0.txt'

with open(full, encoding="utf-8") as file:
    InBuff = file.read()




# Preparing ------------------------------

from re import compile

# https://docs.python.org/3/howto/regex.html


InData = [
        tuple( int(s) for s in m[4:-1].split(',') )
        for m in compile(r"mul\(\d+,\d+\)").findall(InBuff)
]




# Digestion ------------------------------

from itertools import starmap
from operator import mul

# https://docs.python.org/3/library/itertools.html#itertools.starmap
# https://docs.python.org/3/library/operator.html


ans = sum(starmap(mul,InData))
print(ans)