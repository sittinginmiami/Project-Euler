# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def less_than_twenty(num):
    switch =  {
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8}
    return switch.get(num,0)


def two_digit_letters(number):
    if number < 20:
        return less_than_twenty(number)
    elif number < 40:
        return 6 + less_than_twenty(number%10)
    elif number < 70:
        return 5 + less_than_twenty(number%10)
    elif number < 80:
        return 7 + less_than_twenty(number%10)
    else:
        return 6 + less_than_twenty(number%10)


total_letters = 0

for x in range(1,100):
    total_letters += two_digit_letters(x)

total_letters *= 10

total_letters += 6300+3*99*9

for x in range(1, 10):
    total_letters += less_than_twenty(x)*100

for x in range(1000, 1001):
    total_letters += 11





print("Total number of letters = " + str(total_letters) + ".")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
