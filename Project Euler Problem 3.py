# projecteuler.net problem #3
#
# this problem will find the largest prime factor of 600851475143
#
#
largest_prime_factor = 1
prime_factor_temp = 1
test_factor = 2
number = 600851475143
while number > 1:
    if (number % test_factor) == 0:
        number /= test_factor
        if test_factor > largest_prime_factor:
            largest_prime_factor = test_factor
    else :
        test_factor +=1
print(largest_prime_factor)
    
