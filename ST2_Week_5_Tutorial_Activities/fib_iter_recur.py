import timeit

def fibonacci_rec(n):
    if n <= 0:
        return 0 # Base case
    elif n == 1:
        return 1 # Base case 
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2) # Recursive case


def fibonacci_iter(n):
    fib =[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
fibonacci_iter_result = timeit.timeit(lambda: fibonacci_iter(30), number=10)
fibonacci_rec_result = timeit.timeit(lambda: fibonacci_rec(30), number=10)
print(f"Iterative Fibonacci calculation took: {fibonacci_iter_result:.6f} seconds")
print(f"Recursive Fibonacci calculation took: {fibonacci_rec_result:.6f} seconds")