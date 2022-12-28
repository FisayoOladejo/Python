#This game prgrame is build with python while loop

secre_number=9 
guess_count =0
guess_limit= 3

while guess_count < guess_limit:
    guess =int(input("Please enter your number: "))
    guess_count +=1
    if guess == secre_number:
        print("You won!")
        break
else:
    print("Sorry you fail")

