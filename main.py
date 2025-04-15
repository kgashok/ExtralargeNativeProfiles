
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Calculate powers of 1.01 and fibonacci numbers
base = 1.01
exponents = [10, 60, 100, 180, 200, 300, 365, 700]

# First table: Power calculations
print("Power of 1.01 Calculations:")
print("-" * 80)

prev_exp = exponents[0]
prev_result = base ** prev_exp
print(f"1.01^{prev_exp:3d} = {prev_result:8.2f}")

for exp in exponents[1:]:
    result = base ** exp
    exp_increase = ((exp - prev_exp) / prev_exp) * 100
    value_increase = ((result - prev_result) / prev_result) * 100
    
    print(f"1.01^{exp:3d} = {result:8.2f} | Exponent increase: {exp_increase:7.1f}% | Value increase: {value_increase:8.1f}%")
    
    prev_exp = exp
    prev_result = result

# Second table: Fibonacci calculations
print("\nFibonacci Sequence Values:")
print("-" * 80)
prev_exp = exponents[0]
prev_fib = fibonacci(prev_exp)
print(f"Fib({prev_exp:3d}) = {prev_fib:8d}")

for exp in exponents[1:]:
    fib = fibonacci(exp)
    exp_increase = ((exp - prev_exp) / prev_exp) * 100
    value_increase = ((fib - prev_fib) / prev_fib) * 100
    
    print(f"Fib({exp:3d}) = {fib:8d} | Exponent increase: {exp_increase:7.1f}% | Value increase: {value_increase:8.1f}%")
    
    prev_exp = exp
    prev_fib = fib
