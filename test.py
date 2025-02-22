def getAge():
    birth_year = int(input("Please enter your birth year: "))
    boolean = input("Have you had your birthday yet? (Yes or No)\n")
    if boolean == "Yes":
        year = 2025
    else:
        year = 2024
    age = year - birth_year
    return age

def getPet():
    pet = input("What is your pet's name? ")
    return pet