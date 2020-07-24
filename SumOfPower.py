"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import math

number = int(math.pow(2,1000))
finalNum = 0
out = [int(i) for i in str(number)]

for j in out:
    finalNum += j

print(finalNum)
