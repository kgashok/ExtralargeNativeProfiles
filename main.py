
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# First table: Power calculations
base = 1.01
exponents = [10, 60, 100, 180, 200, 300, 365, 700]

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

# Second table: Selected Fibonacci numbers
print("\nSelected Fibonacci Numbers:")
print("-" * 80)
selected_numbers = [1, 3, 6, 10, 12, 16, 18, 20, 24]
prev_exp = selected_numbers[0]
prev_fib = fibonacci(prev_exp)
print(f"Fib({prev_exp:3d}) = {prev_fib:8d}")

for exp in selected_numbers[1:]:
    fib = fibonacci(exp)
    exp_increase = ((exp - prev_exp) / prev_exp) * 100
    value_increase = ((fib - prev_fib) / prev_fib) * 100
    print(f"Fib({exp:3d}) = {fib:8d} | Exponent increase: {exp_increase:7.1f}% | Value increase: {value_increase:8.1f}%")
    prev_exp = exp
    prev_fib = fib

# Third table: Bamboo Growth Pattern
print("\nBamboo-like Growth Pattern:")
print("-" * 80)
# Using exponential growth with dormancy period
bamboo_years = [1, 2, 3, 4, 4.5, 5]
initial_height = 0.1  # Initial underground growth in meters

prev_year = bamboo_years[0]
prev_height = initial_height
print(f"Year {prev_year:3.1f} = {prev_height:8.2f}m")

for year in bamboo_years[1:]:
    # Dramatic growth in final year
    if year >= 4:
        height = initial_height * (1.5 ** (year * 52))  # Weekly growth explosion
    else:
        height = initial_height * (1.1 ** year)  # Slow underground growth
    
    year_increase = ((year - prev_year) / prev_year) * 100
    height_increase = ((height - prev_height) / prev_height) * 100
    print(f"Year {year:3.1f} = {height:8.2f}m | Time increase: {year_increase:7.1f}% | Height increase: {height_increase:8.1f}%")
    prev_year = year
    prev_height = height
