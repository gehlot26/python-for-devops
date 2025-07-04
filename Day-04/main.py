from temperature import conversion

c_temp = 32
f_temp = 98.6

print(f"{c_temp}°C is equal to {conversion.celsius_to_fahrenheit(c_temp)}°F")
print(f"{f_temp}°F is equal to {conversion.fahrenheit_to_celsius(f_temp)}°C")