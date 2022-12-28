def school_age_cal(age, name):
    if age < 1:
        print("Enjoy the time", name, "is only", age)
    elif age <=2: 
        print("now", name, "is ready for creche")
    elif age ==3:
        print("Time to start kindergarten", name, "is now", age, "years old")
    else:
        print(name, "grow up so very fast")
school_age_cal(1, "Blosom")
