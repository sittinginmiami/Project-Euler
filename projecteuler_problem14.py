# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def length_of_Collatz(number):
    # Use a breakpoint in the code line below to debug your script.
    counter = 1
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        counter += 1
        # print(counter)
    return counter


# Press the green button in the gutter to run the script.
longest_array = 1
longest_x = 1

for x in range(1, 1000000):
    # print(x)
    this_array_length = length_of_Collatz(x)
    # print(this_array_length)
    if this_array_length > longest_array:
        print(x, this_array_length, longest_array, longest_x)
        longest_array = this_array_length
        longest_x = x


print("The longest array was " + str(longest_array) + " in length.")
print("The longest series came from number " + str(longest_x) + ".")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
