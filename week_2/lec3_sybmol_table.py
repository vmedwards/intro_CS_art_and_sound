"""
Victoria Edwards
04/06/2026
Course: ES1093

Example for Symbol Table and Control flow 
"""

# Define functions
def diff(a, b):
    d = a - b # Compute the difference
    return(d) # return the difference to the main code 

def half(a):
    divideBy = 2.0
    h = a / divideBy
    return(h)

# Main code goes here
x = 10
y = 15
z = diff(10, 15)
z = diff(x ,y )
y = half(6)
z = diff(x, y)
