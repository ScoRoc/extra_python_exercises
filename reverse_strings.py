# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***

def flip(string):
    arr = string.split(' ')
    newArr = []
    for i in range(len(arr)):
      newArr.append(arr[i][len(arr[i])::-1])
    print(' '.join(newArr))

flip('here is a sentence')
