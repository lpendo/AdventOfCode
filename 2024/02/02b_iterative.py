# import urllib.request as req Target =
# 'https://adventofcode.com/2024/day/1/input'
# # From https://docs.python.org/3/howto/urllib2.html
# with req.urlopen(Target) as response: Input = response.open()
# 
# Above will require more work with the AoC API to deal with authentication.
# Also need to figure out how to use urllib2 to supply cookies/tokens.


# Gathering ------------------------------

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/stdtypes.html#str

# using dl'd file from AoC website
full = 'input.txt'
test0 = 'test0.txt'

with open(test0, encoding="utf-8") as file:
    InBuff = file.read()

InBuff = [s.split() for s in InBuff.split('\n')]
InBuff = [ [ int(xs) for xs in s ] for s in InBuff if len(s) != 0 ]

# Preparing ------------------------------

from itertools import pairwise

# https://docs.python.org/3/howto/sorting.html
# https://docs.python.org/3/library/itertools.html#itertools.pairwise

Prepped = [ [ b-a for a,b in pairwise(xs) ] for xs in InBuff ]

# Prepped is a list of lists of differences between elements of sequences taken
# from each line of the input file.



# Digestion ------------------------------

# https://docs.python.org/3/tutorial/controlflow.html

ans = 0
for n,ds in enumerate(Prepped):

    print("New line --------------------------------------------------")
    print(InBuff[n])
    print(ds)

    d0 = ds[0]
    d1 = ds[1]

    x01 = d0*d1
    
    if ( x01 < 0 ) :
        


    # We only get to drop a number from a sequence once.
    Flag = False
    while len(ds) > 0 :

        print( "In loop(", n, ") :  ", ds)

        # Analyze first three or four elements. This necessary to establish if
        # the sequence should be understood to increasing or decreasing.

        # Consider differences
        # d0 := s1 - s0
        # d1 := s2 - s1
        # d2 := s3 - s2

        d0 = ds[0]
        d1 = ds[1]
        d2 = ds[2]

        ds = []






print("Ans ------------------------")
print(ans)

