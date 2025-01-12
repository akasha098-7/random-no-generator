import random

def random_number_generator():
    print("Welcome to the Random Number Generator!")
    print("Choose the range for generating a random number.")
    try:
        lower_limit = int(input("Enter the lower limit: "))
        upper_limit = int(input("Enter the upper limit: "))
        
        if lower_limit > upper_limit:
            print("The lower limit must be less than or equal to the upper limit.")
            return
        
        random_number = random.randint(lower_limit, upper_limit)
        print(f"Your random number between {lower_limit} and {upper_limit} is: {random_number}")
    except ValueError:
        print("Please enter valid numbers for the limits.")

random_number_generator()

