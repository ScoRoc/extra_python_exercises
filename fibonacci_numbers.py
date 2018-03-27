# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***

def find_fib(fibLen):
    fibArr = [0, 1]
    for i in range(fibLen - 1):
        n = fibArr[len(fibArr) - 1] + fibArr[len(fibArr) - 2]
        fibArr.append(n)
    print(fibArr)

find_fib(10)
