# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Show the result
print("Fahrenheit:", fahrenheit)
print("Conversion complete.")
# Kelvin = Celsius + 273.15 (0 degrees Celsius equals 273.15 K; the Kelvin scale starts at absolute zero)
kelvin = celsius + 273.15
print(f"{celsius} C = {kelvin:.2f} K")