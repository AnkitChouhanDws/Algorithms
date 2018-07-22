'''
This is python code to find Nth number in fibonacci sequence using Dynamic Programming(using memoization technique to store values)
'''
'''
lookup[] is the list which contains the fibonacci sequence.
Initialise all the positions of lookup with -1 or None
'''

lookup=[-1]*100

def fib(n):
    if lookup[n]==-1:
        if n<=1:
            lookup[n]=n
        else:
            lookup[n]=fib(n-1)+fib(n-2)
    return lookup[n]
    
'''
Driver Code
'''
'''
Example- find the fibonaaci number at 5th position
'''
print(fib(5))
