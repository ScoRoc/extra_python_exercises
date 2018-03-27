# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***

def pyramid(h):
    p = '#'
    s = ' '
    n = h
    for i in range(h):
        print((s * (n - 1)) + p * (h + 1 - n))
        n -= 1

pyramid(6)

def pyramidFull(h):
    p = '#'
    s = ' '
    n = h
    for i in range(h):
        print((s * (n - 1)) + p * (h + 1 - n) + ' ' + p * (h + 1 - n) + (s * (n - 1)))
        n -= 1

pyramidFull(6)
