#
# Project Euler problem 1
# This program will sum all natural numbers under 1000 that are multiples of 3 or 5
#
sum = 0
for i in range(1, 1000):
    if i % 3 == 0:
        sum += i
    else:
        if i % 5 == 0:
            sum += i
print(sum)
        
