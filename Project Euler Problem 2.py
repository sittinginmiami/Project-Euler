# Project Euler problem 2
#
# This program will sum all the even terms of the Fibonacci sequence which are less than 4 million
#
#
sum = 0
fib_term_i = 1
fib_term_plus1 = 1
fib_term_plus2 = 2
while fib_term_plus2 < 4000000:
    if (fib_term_plus2 % 2) == 0:
        sum += fib_term_plus2
    fib_term_i = fib_term_plus1
    fib_term_plus1 = fib_term_plus2
    fib_term_plus2 = fib_term_i + fib_term_plus1
print(sum)
