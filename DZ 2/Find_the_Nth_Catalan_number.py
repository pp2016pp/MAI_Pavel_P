from math import factorial

def nth_catalan_number(n):
    return factorial(2*n)//factorial(n+1)//factorial(n)
