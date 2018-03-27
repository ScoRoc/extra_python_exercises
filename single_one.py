# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***

def single(intArr):
    for i in intArr:
        if intArr[i] != intArr[i-1] and intArr[i] != intArr[i+1]:
            print(intArr[i])

single([1,1,2,2,3,3,4,5,5,6,6,7,7])

def single2(arr):
  nArr = arr
  nArr.sort()
  for i in range(len(nArr)):
    print(nArr[i])
    # if i == (len(nArr) - 1):
      # print(nArr[i])
  print(nArr)

single2([1,1,2,3,3,4,4,5,6,6,7,7,9,9,8,8])

def find(a):
  return [x for x in a if a.count(x) < 2][0]

print(find([1,1,2,3,3,4,4,5,5,6,6,7,7,9,9,8,8]))
