
#projecteuler.net problem 11
#
# this program will find the largest multiple of 4 digits in a row (up/down/diagonal/right/left) in a particular given grid of numbers
#
#
#
#additional rows and columns of zeros were added so that our loops can be simplified / minimized.  Clearly, the zero calculations when
#multiplying will Not be a maximum since all the numbers are positives
number_grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8, 0, 0, 0],
                         [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0, 0, 0, 0],
                         [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65, 0, 0, 0],
                         [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91, 0, 0, 0],
                         [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80, 0, 0, 0],
                         [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50, 0, 0, 0],
                         [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70, 0, 0, 0],
                         [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21, 0, 0, 0],
                         [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 0, 0, 0],
                         [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95, 0, 0, 0],
                         [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92, 0, 0, 0],
                         [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57, 0, 0, 0],
                         [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58, 0, 0, 0],
                         [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40, 0, 0, 0],
                         [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66, 0, 0, 0],
                         [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 0, 0, 0],
                         [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36, 0, 0, 0],
                         [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16, 0, 0, 0],
                         [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54, 0, 0, 0],
                         [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#
#we will now set a maximum multiple variable and initialize it to one since by inspection the max is greater than 1
max_value = 1
max_row_location = 0
max_column_location = 0
#
# we will now set row and column variables to use as counters
row = 0
column = 0
while row < 20:
    column = 0 #resets column to beginning of row
    while column < 20:
        temp_value = 1
        for right in range(0, 4): # checks the multipel of 4 consecutive digits going right
            temp_value *= number_grid[row][column + right]
        if temp_value > max_value:
            max_row_location = row
            max_column_location = column
            max_value = temp_value  #replaces max_value with temp_value of this multiple is larger than the largest we've found so far
        temp_value = 1 # reset temp_value
        for down in range(0, 4): # checks the multiple of 4 consecutive digits going down
            temp_value *= number_grid[row + down][column]
        if temp_value > max_value:
            max_row_location = row
            max_column_location = column
            max_value = temp_value  #replaces max_value with temp_value of this multiple is larger than the largest we've found so far
        temp_value = 1 # reset temp_value
        for downright in range(0, 4): # checks the multiple of 4 consecutive digits going down+right diagonally
            temp_value *= number_grid[row + downright][column + downright]
        if temp_value > max_value:
            max_row_location = row
            max_column_location = column
            max_value = temp_value  #replaces max_value with temp_value of this multiple is larger than the largest we've found so far
        temp_value = 1
        if row > 2:
            for upright in range(0, 4): # checks the multiple of 4 consecutive digits going up+right diagonally
                temp_value *= number_grid[row - upright][column + upright]
            if temp_value > max_value:
                max_row_location = row
                max_column_location = column
                max_value = temp_value  #replaces max_value with temp_value of this multiple is larger than the largest we've found so far
        temp_value = 1
        column += 1
    row += 1
print(max_value)
print(max_row_location)
print(max_column_location)
        
        

