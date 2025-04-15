
# Calculate powers of 1.01 for different exponents
base = 1.01
exponents = [10, 60, 100, 180, 200, 300, 365, 700]

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
