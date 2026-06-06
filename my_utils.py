def calculate_average(numbers):
    return sum(numbers) / len(numbers)

n = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(calculate_average(numbers))


def format_currency(amount):
    return f"${amount:.2f}"
amount = float(input("Enter an amount: "))
formatted_amount = format_currency(amount)      
print(f"The formatted amount is: {formatted_amount}")   

def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False    
email = input("Enter your email address: ")
if validate_email(email):   
    print("Valid email address.")           
else:    print("Invalid email address.")    


def generate_greeting(name, time_of_day):
    return f"Good {time_of_day}, {name}! Welcome to the world of programming."
name = input("Enter your name: ")
time_of_day = input("Enter the time of day (morning, afternoon, evening): ")
print(generate_greeting(name, time_of_day))


def convert_temperature(temp, unit):
    if unit == "C":
        return f"{(temp * 9/5) + 32} °F"
    elif unit == "F":
        return f"{(temp - 32) * 5/9} °C"
    else:
        return "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")  
print(convert_temperature(temp, unit))  
