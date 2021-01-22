# projecteuler.net
# This program will calculate the difference between the sum of the squares of 1,...,100 and the square of the sums
# we will use simple brute force calculations
sum_of_the_squares = 0
square_of_the_sum = 0
temp_sum = 0
difference = 0

#this for loop directly keeps adding squares to sum_of_the_squares
#this loop also adds up the first 100 natural numbers to use later 
for i in range(1, 101):
    sum_of_the_squares += i*i
    temp_sum += i
    
#below, we square the sum we calculated in the for loop to get square_of_the_sum
square_of_the_sum = temp_sum * temp_sum

#below, we subtract the 2 numbers to find the difference
difference = sum_of_the_squares - square_of_the_sum

#this line prints the calculated difference to the console
print(difference)

