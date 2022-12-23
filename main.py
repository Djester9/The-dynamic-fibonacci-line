#import time module in order to slow print
import time


#Define function which returns True if n is a Fibonacci number, False otherwise.
def is_fibonacci(n):
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        # Generate the Fibonacci sequence up to n
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return n in fib

#asigning variables
line = '|'
count = 0



while count < 1000000: #run 1mil times
    if is_fibonacci(count):
        line = ' |'
    print(line)
    time.sleep(.8)
    count += 1
    line = '|'
