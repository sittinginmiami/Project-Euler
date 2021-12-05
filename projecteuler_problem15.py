

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def recursive_rectangle(length, width):
    # Use a breakpoint in the code line below to debug your script.
    counter = 0
    if width == 1 and length == 1:
        return 2  # Press Ctrl+F8 to toggle the breakpoint.
    else:
        if width == 1:
            return 1 + recursive_rectangle(length - 1, width)
        else:
            if length == 1:
                return 1 + recursive_rectangle(length, width - 1)
            else:
                counter += recursive_rectangle(length - 1, width)
                counter += recursive_rectangle(length, width - 1)
                return counter


# Press the green button in the gutter to run the script.
howManyPaths = recursive_rectangle(20, 20)
print(howManyPaths)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
