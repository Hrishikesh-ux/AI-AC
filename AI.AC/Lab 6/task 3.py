def classify_age(age):
    if age < 0:
        print("Invalid age")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59: 
        print("Adult")  
    else:
        print("Senior")
age_input=int(input("Enter age: "))
classify_age(age_input)        