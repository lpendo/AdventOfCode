# import urllib.request as req Target =
# 'https://adventofcode.com/2024/day/1/input'
# # From https://docs.python.org/3/howto/urllib2.html
# with req.urlopen(Target) as response: Input = response.open()
# 
# Above will require more work with the AoC API to deal with authentication.


# Gathering ------------------------------

# using file from AoC website
full = 'input.txt'
test0 = 'test0.txt'


# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
with open(test0, encoding="utf-8") as file:
    InData = file.read()




# Preparing ------------------------------

# https://docs.python.org/3/library/stdtypes.html#str
Prepped = [s.split() for s in InData.split('\n')]
Prepped = [ ( int(s[0]) , int(s[1]) ) for s in Prepped if len(s) != 0]

# https://docs.python.org/3/howto/sorting.html
Prepped = sorted( xs[0] for xs in Prepped ), sorted( xs[1] for xs in Prepped )

# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter
counts = Counter(tuple(Prepped[1]))


# Digestion ------------------------------

ans = sum( counts[xs]*xs for xs in Prepped[0] if xs in counts )

print(ans)

