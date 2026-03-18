import timeit

def sum_of_natural_numbers_rec(n):
    if n == 1:
        return 1 # Base case
    else:
        return n + sum_of_natural_numbers_rec(n - 1) # Recursive case

def sum_of_natural_numbers_iter(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

sum_iter_result = timeit.timeit(lambda: sum_of_natural_numbers_iter(100), number=10)
sum_rec_result = timeit.timeit(lambda: sum_of_natural_numbers_rec(100), number=10)
print(f"Iterative sum of first 100 natural numbers took: {sum_iter_result:.6f} seconds")
print(f"Recursive sum of first 100 natural numbers took: {sum_rec_result:.6f} seconds")
