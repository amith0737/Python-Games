def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Choose an option:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice not in [1, 2]:
            print("Invalid choice! Please select 1 or 2.")
            return

        temperature = float(input("Enter the temperature to convert: "))
        
        if choice == 1:
            converted = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F")
        elif choice == 2:
            converted = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    temperature_converter()
