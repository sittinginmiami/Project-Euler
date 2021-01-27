#projecteuler.net problem 9
#
#this program will find the Pythagorean tripe where a + b + c = 1000
#
#
for a in range(1,500):
    for b in range(a+1,998):
        c = 1000 - b - a
        if (a * a) + (b * b) == (c * c):
            print(a*b*c)
        b += 1
    a+=1

        
