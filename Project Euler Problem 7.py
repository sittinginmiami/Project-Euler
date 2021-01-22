# projecteuler.net problem 7
#
# this program will find the 10001st prime number by counting the primes as we find them
# while we check each natural number to see whether it is prime.
#
#

def isPrime(n):
    if n <= 1 or n % 1 > 0:
      return False
    for i in range(2, round(x/2)+1):
       if n % i == 0:
           return False
    return True

# we will use x as a placeholder as we work through the natural numbers checking each one
x = 2
#This variable will keep track of how many primes we've found
counter = 0
while counter<10001:
    if isPrime(x):
        #print(x)
        counter += 1
    x += 1
print(x-1)


