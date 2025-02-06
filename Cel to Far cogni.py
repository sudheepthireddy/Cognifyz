def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9
def main():
    while True:
        try:
            temp = float(input("Enter the temperature value (or type 'exit' to quit):"))
            unit = input("Enter the unit (c for celsius, f for fahrenheit):").strip().upper()
            if unit == "C":
                converted = celsius_to_fahrenheit(temp)
                print(f"{temp}°C is equal to {converted:.2f}°F")
            elif unit == "C":
                converted = fahrenheit_to_celsius(temp)
                print(f"{temp}°F is equal to {converted:.2f}°C")
            else:
                print("Invalid unit. please enter C for celsius or F for fahrenheit.")
            cont = input("Do you want to convert another temperature? (yes/no):").strip().lower()
            if cont != 'yes':
                break
        except ValueError:
            print("Invalid input.please enter a numeric temperature value.")
if __name__ == "__main__":
    main()