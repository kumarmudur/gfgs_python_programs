# Function for nth Fibonacci number 

# method 1 recursion
def fibonacci(n):
    if n < 0:
        print('Incorrect input')
    # First Fibonacci number is 0 
    elif n == 1:
        return 0
    # Second Fibonacci number is 1 
    elif n == 2:
        return 1
    else:
        return fibonacci(n) + fibonacci(n - 1)


# method 2 (use dynamic programming)

# Function for nth fibonacci number - Dynamic Programing 
# Taking 1st two fibonacci nubers as 0 and 1 

fib_array = [ 0, 1]

def fibonacci1(n):
    if n < 0:
        print('Incorrect input')
    elif n <= len(fib_array):
        return fib_array[n-1]
    else:
        temp_fib = fibonacci1(n-1) + fibonacci1(n-2)
        fib_array.append(temp_fib)
        return temp_fib


