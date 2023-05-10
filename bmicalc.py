height = input("Enter height in m: ")
weight = input("Enter weight in kg: ")

bmi = float(weight) / float(height) ** 2

# Whole num with rounding
# f-string: (f"string {variable}")
print(f"Whole number rounding: {round(bmi)}")

# Rounding with 2 decimal place
# rounding decimal: round(number, decimal_point)
print(f"two decimal place: {round(bmi, 2)}")

# OR BMI as whole number (no rounding)
print(f"Whole number no rounding: {int(bmi)}")

