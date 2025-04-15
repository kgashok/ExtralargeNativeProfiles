
# Calculate powers of 1.01 for different exponents
base = 1.01
exponents = [10, 60, 100, 180, 200, 300, 365, 700]

for exp in exponents:
    result = base ** exp
    print(f"1.01^{exp} = {result:.2f}")
