import math

print("==========================================")
print("        ENGINEERING CALCULATION TOOL      ")
print("==========================================")


value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal_val = float(input("Enter a decimal measurement: "))


power_res = math.pow(value, exponent)
sqrt_res = math.sqrt(value)
ceil_res = math.ceil(decimal_val)
floor_res = math.floor(decimal_val)


print("-- Results ---")
print(f"  Value               : {value:.1f}")
print(f"  Exponent            : {exponent:.1f}")
print(f"  Power (pow)         : {power_res:.1f}")
print(f"  Square Root (sqrt)  : {sqrt_res:.4f}")
print(f"  Decimal Value       : {decimal_val:.1f}")
print(f"  Ceil Value          : {ceil_res}")
print(f"  Floor Value         : {floor_res}")
print("==========================================")