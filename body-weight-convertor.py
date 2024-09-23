# Write a program that asks for a user’s body weight in pounds (lbs) and converts it to kilograms (kg).

# Lab2: body-weight-convertor.py

# Asking for body weight in pounds
weight_in_lbs = int(input("my body weight in pounds this month has been (lbs):\t"))

# Converting to kilograms (1 pound = 0.453592 kg)
weight_in_kg = weight_in_lbs * 0.453592

# Displaying the result with three decimal places(.3f)
print(f"my body weight is {weight_in_lbs} lbs, and the equivalent in kgs is {weight_in_kg:.3f} kg. Thank you!")