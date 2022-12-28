#This code collect input from users and check if users are hae not violate character length set 
word_length = input("Hey you can type here: ")

if len(word_length) < 3:
    print("Hey atleast 3 characters long must be type")

elif len(word_length) == 3:
    print("Hey just 3 character types not look good! you can do better")

elif len(word_length) ==50:
    print("Hey look good! you are on the right track in building your writen skills")
else:
    print("You hae exceeded the character max limit")    



