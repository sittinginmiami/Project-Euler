#projecteuler.net problem 5
#
#this will find the smallest number that is evenly divided by number 1 through 20
#
#
keep_going = True
test_number = 21
while keep_going:
    if test_number % 20 == 0:
        if test_number % 19 ==0:
            if test_number % 9 == 0:
                if test_number % 17 == 0:
                    if test_number % 16 == 0:
                        if test_number % 5 == 0:
                            if test_number % 7 == 0:
                                if test_number % 13 == 0:
                                    if test_number % 11 == 0:
                                        keep_going = False
                                    else:
                                        test_number += 1
                                else:
                                    test_number += 1
                            else:
                                test_number += 1
                        else:
                            test_number += 1
                    else:
                        test_number += 1
                else:
                    test_number += 1
            else:
                test_number += 1
        else:
            test_number += 1
    else:
        test_number += 1
print(test_number)
        
