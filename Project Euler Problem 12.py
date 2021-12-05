# projecteuler.net problem 12
#
# this program will find the first triangle number that has over 500 divisors.
#
#
import math

# method to count the divisors 
def countDivisors(number) : 
    count = 0  
    # Note that this loop runs till square root 
    i = 1
    while i <= math.sqrt(number): 
          
        if (number % i == 0) : 
              
            # If divisors are equal, count only one 
            if (number / i == i) : 
                count += 1 
            else : 
                # Otherwise count both 
                count += 2 
        i = i + 1
  
    return count

nth_triangle_number = 1
n = 1
greater_than_5 = False


while not(greater_than_5) :
    if countDivisors(nth_triangle_number) > 500: greater_than_5 = True
    n = n+1
    nth_triangle_number = nth_triangle_number + n
    

print("***")
print(nth_triangle_number-n)
print(n-1)
print(countDivisors(nth_triangle_number-n))
            
    
