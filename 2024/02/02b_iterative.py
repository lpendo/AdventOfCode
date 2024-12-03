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

        # A differences list of length one represents the sequence s0, s1.
        # This passes if abs(d0) meets our criteria
        if len(ds) == 1: 
            if abs(ds[0]) >= 1 and abs(ds[0]) <= 3 : 
                ans += 1


                print("here!")



            else:
                if Flag : break
                ans += 1


                print("here!")



            ds = []
            continue

        d0 = ds[0]
        d1 = ds[1]

        # s0 == s1 == s2 -- Too many to eject. Shut it down!
        if d0+d1 == 0 : break

        x01 = d0*d1

        # ds[0]+ds[1] != 0 is True
        if x01 == 0 :
            # Either s1 == s0, or s1 == s2. We can eject s1.
            if Flag : break
            Flag = True # Ejected!
            # s1 ejected -- equivalent to (s2-s0) = d0 + d1
            # loop for s0, s2, s3, ...
            ds = [ d0 + d1 ] + ds[2:]
            if abs(ds[0]) < 1 or abs(ds[0]) > 3 : break  # Eject!
            continue

        # Need to check if d2 exists
        if len(ds) > 2 :
            d2 = ds[2]

            # Recall d0=s1-s0, d1=s2-s1. and d2=s3-s2

            # x01 != 0 is True
            if d2 == 0 :
                # s0 / s1 / s2 == s3
                # We can eject s2.
                if Flag : break
                Flag = True # Ejected!
                    
                # Ejecting s2 equivalent to 
                # d2' := s3 - s1 = d1 + d2

                # s0 / s1 / s3 must be true
                ds = ds[:1] + [ d1 + d2 ] + ds[3:]
                if abs(ds[1]) < 1 or abs(ds[1]) > 3 : break  # Eject!
                continue


            x02 = d0*d2
            x12 = d1*d2

            # Below, documentation use the forms { x / y } and { x % y }. 
            # The { / } and { % } represent opposed comparative operations
            if ( x01 > 0 ) and ( x02 > 0 ) :
                # d0, d1, d2 are all same sign, nonzero
                # s0 / s1 / s2 / s3
                # check that d0 meets criteria
                if abs(d0) < 1 or abs(d0) > 3 :
                    # d0 does not meet criteria -- s1 to be ejected.
                    if Flag : break
                    Flag = True # Ejected!

                    # Ejecting s1 equivalent to 
                    # d0' := s2 - s0 = d0 + d1
                    # d1' := s3 - s2 = d2

                    # s0 / s2 / s3 must be true once s1 ejected
                    # Check d0' * d1' = x02 + x12 > 0
                    if ( x02 + x12 ) > 0 :
                        # Ejected s1 -- [ d0+d1 ] + [ d2, ... ]
                        ds = [ d0+d1 ] + ds[2:]
                        if abs(ds[0]) < 1 or abs(ds[0]) > 3 : break  # Eject!
                        continue

                # s0 accepted!
                # if s1 isn't too big
                # s0 can safely fall off front of sequence
                # loop for s1, s2, s3, ...
                if abs(d1) < 1 or abs(d1) > 3 :
                    break # Eject!
                else:
                    ds = ds[1:]
                    continue

            if ( x01 < 0 ) and ( x02 > 0 ) :
                # d0 and d2 are same sign, d1 is different sign
                # s0 / s1 % s2 / s3
                
                # To fix this we must eject s1 or s2!
                if Flag : break
                Flag = True # Ejected!

                # 0 / d0 = s1 - s0
                # 0 % d1 = s2 - s1
                # 0 / d2 = s3 - s2

                # Ejecting s1 equivalent to 
                # d0' := s2 - s0 = d0 + d1
                # d1' := s3 - s2 = d2

                # s0 / s2 / s3 must be true once s1 ejected
                # Check d0' * d1' = x02 + x12 > 0


                # Ejecting s2 equivalent to 
                # d0' := s1 - s0 = d0
                # d1' := s3 - s1 = d1 + d2

                # s0 / s1 / s3 must be true once s1 ejected
                # Check d0' * d1' = x01 + x02 > 0


                # Too many to eject. Shut it down!
                if ( x02 + x12 ) <= 0 and ( x01 + x02 ) <= 0 : break

                if ( x02 + x12 ) > 0 :
                    # Ejected s1 -- [ d0+d1, d2 ] + [d3, ... ]
                    dx = [ d0+d1, d2 ]
                    if abs(dx[0]) < 1 or abs(dx[0]) > 3 : break # Eject!
                
                if ( x01 + x02 ) > 0 :
                    # Ejected s2 -- [ d0, d1+d2 ] + [d3, ...]
                    dx = [ d0, d1+d2 ]
                    if abs(dx[1]) < 1 or abs(dx[1]) > 3 : break # Eject

                ds = dx + ds[3:]


            if ( x01 < 0 ) and ( x12 > 0 ) :
                # d1 and d2 are same sign, d0 is different sign
                # s0 % s1 / s2 / s3

                # Will need to eject either s0, s1
                if Flag : break
                Flag = True # Ejected!

                # check if the difference d1=s2-s1 meets criteria
                if abs(d1) < 1 or abs(d1) > 3 :
                    # s1 ejected! Equivalent to 
                    # d0' := s2 - s0 = d0 + d1
                    # d1' := s3 - s2 = d2

                    # Ejected s1 -- [ d0+d1, d2 ] + [d3, ... ]
                    ds = [ d0+d1, d2 ] + ds[3:]
                    if abs(d0+d1) < 1 or abs(d0+d1) > 3 : break 
                    continue
                else:
                    # s0 ejected!
                    # loop for s1, s2, s3, ...
                    ds = ds[1:]
                    continue



            if ( x01 > 0 ) and ( x02 < 0 ) :
                # d0 and d1 are same sign, d2 is different sign
                # s0 / s1 / s2 % s3

                # To fix this we must eject s2 or s3!
                if Flag : break
                Flag = True # Ejected!

                # 0 / d0 = s1 - s0
                # 0 / d1 = s2 - s1
                # 0 % d2 = s3 - s2

                # Ejecting s2 equivalent to 
                # d0' := s1 - s0 = d0
                # d1' := s3 - s1 = d1 + d2

                # s0 / s1 / s3 must be true once s2 ejected
                # Check d0' * d1' = x01 + x02 > 0

                if ( x01 + x02 ) > 0:
                        # if s3-s1 = d1 + d2 meets criteria
                        # then eject s2
                        if abs(d1+d2) < 1 or abs(d1+d2):
                            # s2 ejected!
                            # [ ..., d1 ] + [ d2+d3 ] + [ d4, ... ]
                            ds = ds[:2] + [ d1 + d2 ] + ds[3:]


                # Ejecting s3 equivalent to 
                # d1' := s2 - s1 = d1
                # d2' := s4 - s2 = d2 + d3

                # s0 / s1 / s2 must be true once s1 ejected
                # Check d1' * d2' = x12 + x23 > 0
                if len(ds) > 3:

                    d3 = ds[3]
                    x23 = d2*d3

                    # s0 / s1 / s2 % s3 % s4 -- this doesn't work
                    # Too many to eject. Shut it down!
                    if ( x23 ) <= 0 : break

                    # s0 / s1 / s2 % s3 / s4
                    if ( x23 ) > 0 :

                        # if s4-s2 = d2 + d3 meets criteria
                        # then eject s3                    
                        if abs(d2+d3) < 1 or abs(d2+d3):
                            # s3 ejected!
                            # [ ..., d1 ] + [ d2+d3 ] + [ d4, ... ]
                            ds = ds[:2] + [ d2 + d3 ] + ds[4:]


                # Too many to eject. Shut it down!
                if ( x02 + x12 ) <= 0 and ( x01 + x02 ) <= 0 : break

                if ( x02 + x12 ) > 0 :
                    # Ejected s1 -- [ d0+d1, d2 ] + [d3, ... ]
                    ds = [ d0+d1, d2 ] + ds[3:]
                    continue
                
                if ( x01 + x02 ) > 0 :
                    # Ejected s2 -- [ d0, d1+d2 ] + [d3, ...]
                    ds = [ d0, d1+d2 ] + ds[3:]
                    continue



                else:
                    # len(ds) == 3

                    # if the difference d1=s2-s1 meets criteria
                    if abs(d1) < 1 or abs(d1) > 3 :
                        # s3 ejected
                        # loop for s0, s1, s2
                        ds = ds[:2]
                        continue
                    else :
                        
        else:
            # len(ds) == 2
            if x01 > 0 :
                # d0, d1, d2 are all same sign, nonzero
                # s0 / s1 / s2

                # check that d0, d1 meet criteria
                if abs(d0) < 1 or abs(d0) > 3 :
                    # d0 does not meet criteria -- to be ejected.
                    if Flag : break
                    Flag = True # Ejected!

                # s0 accepted or ejected
                ds = ds[1:]
                continue

                # # s0 accepted!
                # # if s1 isn't too big
                # # s0 can safely fall off front of sequence
                # # loop for s1, s2, s3, ...
                # if abs(d1) < 1 or abs(d1) > 3 :
                #     ds = ds[1:]
                #     continue
                # else:
                #     break # No way to fix big jump in list


            else:
                # d0 and d1 are different signs
                # s0 / s1 % s2
                # Eject s0 !
                if Flag : break
                Flag = True # Ejected!




print("Ans ------------------------")
print(ans)

