def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def celsius_to_kelvin(c):
    return c + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32
def main():
    print("Temperature Converter")
    temp = float(input("Enter temperature value: "))
    unit = input("Enter unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    if unit == 'C':
        print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
        print(f"{temp}°C = {celsius_to_kelvin(temp)}K")
    elif unit == 'F':
        print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
        print(f"{temp}°F = {fahrenheit_to_kelvin(temp)}K")
    elif unit == 'K':
        print(f"{temp}K = {kelvin_to_celsius(temp)}°C")
        print(f"{temp}K = {kelvin_to_fahrenheit(temp)}°F")
    else:
        print("Invalid unit.")
if __name__ == "__main__":
    main()










