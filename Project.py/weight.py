weight= int(input("Hi please enter your weight: "))
unit= input("(L)bs or (k)g?: ")

if unit.upper() == "L" :
    weight*0.454
    a = weight*0.45
    print("your are", a, "kg")
else:
    weight/0.454
    b=weight//0.45
    print("You are", b ,"bs")
