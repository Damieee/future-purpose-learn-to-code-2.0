def welcome_user():
    name = input("Hello, what is your name: ")
    age = int(input("Please enter your age: "))
    city = input("what city are you from? ")
    
    if age < 18:
        return f"Hello {name}, you are not old enough to drive in {city}."
    elif age == 18:
        return f"Hello {name}, you are old enough to drive in {city}."
        
    else:
        return f"Hello {name}, you are too old to drive in this {city}. Get a Bike"
    
print(welcome_user())