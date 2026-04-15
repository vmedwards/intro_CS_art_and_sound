"""
Author: Victoria Edwards
Date: 04/03/2026
Purpose: Live code in class
"""

def getTotal(): 
    left = 10
    right = 3
    middle = 7
    total = left + right + middle 
    print(total)

#getTotal() 
#getTotal()

def getTotalGen(left, middle, right):
    total = left + middle + right
    return(total)

y = getTotalGen(3, 7, 10)
x = getTotalGen(2, 3, 5)
print(x, y)
