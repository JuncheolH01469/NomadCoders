# Example 1
def age_check(age):
    print(f"you are {age}")
    
    if age < 18:
        print("you can't drink")
    else:
        print("enjoy your drink")

age_check(25)

# Example 2
def age_check(age):
    print(f"you are {age}")
    
    if age < 18:
        print("you can't drink")
    elif age == 18:
        print("you are new to this!")
    elif age > 18 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(25)