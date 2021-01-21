# projecteuler.net problem 4
#
# this program will find the largest palindrome made by multiplying 2 three-digit numbers
#
#
def check_palindrome(number):
    string=str(number)
    reverse_string=string[::-1]
    if reverse_string == string:
        return True
    else:
        return False
#
factor_1 = 999
factor_2 = 999
is_this_palindromic = factor_1 * factor_2
#
largest_palindrome = 100001
for i in range(100, 999):
    for j in range(100, 999):
        if check_palindrome(i*j):
            if(i*j)>largest_palindrome:
                largest_palindrome = i*j
print(largest_palindrome)
            
        


    
