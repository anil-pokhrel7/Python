def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")
user_name = input("Enter your name: ")
age_input = input("Enter your age (press Enter to skip): ")
if age_input:
    greet(user_name, int(age_input))
else:
    greet(user_name)