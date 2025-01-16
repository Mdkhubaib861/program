# 1. if statement
def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# 2. if..else statement
def check_age_group(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

# 3. if..elif..else statement
def check_grade(grade):
    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# 4. nested if statement
def check_eligibility(age, is_registered):
    if age >= 18:
        if is_registered:
            print("You are eligible to vote.")
        else:
            print("You need to register before voting.")
    else:
        print("You are not eligible to vote.")

# Testing the functions
print("Testing the if statement:")
check_even_or_odd(7)

print("\nTesting the if..else statement:")
check_age_group(15)

print("\nTesting the if..elif..else statement:")
check_grade(85)

print("\nTesting the nested if statement:")
check_eligibility(20, True)
