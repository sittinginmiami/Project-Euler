#projecteuler.net Problem 10
#
# this program will find the sum of all primes below 2 million
#
#
import math

# this subroutine will check to see if a number is prime or not
def isPrime(n):
    if n <= 1 or n % 1 > 0:
      return False
    for i in range(2, round(math.sqrt(x)) + 1):
       if n % i == 0:
           return False
    return True

#this variable sum will keep track of the sum as primes are added to it
sum=0

#this loop will check each natural number up to 2 million and add it to sum if it is prime
for x in range(1,2000000):
    if isPrime(x):
        sum += x

#this will output the final result to console
print(sum)
