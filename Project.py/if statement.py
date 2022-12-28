studentAge = int(input("Welcome our dear parent please enter your child's age: "))

if studentAge <=1:
    print("Thank you, your child will be enroll in creche\nPlease fill the creche form for your child's assessment with the school chancellor")
    

elif studentAge <=2:
    print("Thank you, your child will be enroll in kindergarten")
    print("Please fill the kindergarten form for your child's assessment with the school chancellor")

elif studentAge ==3:
    print("Thank you, your child will be enroll in primary 1")
    print("Please fill the primary 1 form for your child's assessment with the school chancellor")

elif studentAge == 5:
    print("Thank you, your child will be enroll in primary 2")
    print("Please fill the primary 2 form for your child's assessment with the school chancellor")

else:
    print("Please fill the form to see the school chancellor")