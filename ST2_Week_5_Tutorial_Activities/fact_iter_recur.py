import timeit

def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial_iter_result = timeit.timeit(lambda: factorial_iter(100), number=10)
factorial_rec_result = timeit.timeit(lambda: factorial(100), number=10)
print(f"Iterative factorial calculation took: {factorial_iter_result:.6f} seconds")
print(f"Recursive factorial calculation took: {factorial_rec_result:.6f} seconds")