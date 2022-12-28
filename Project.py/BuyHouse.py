house_price = 1000000
bad_creditcard = 300000
buyer_creditcard = int(input('Welcome enter your credit card balance here: '))

if buyer_creditcard > bad_creditcard:
    print("Please deposite $100000 into our estate agent account")

elif buyer_creditcard == bad_creditcard:
    print("Kindly deposity $200000 into our estate agent account")   

elif buyer_creditcard < bad_creditcard:
    print("You are not eligible to buy this house")

else:
    print("Goodbye") 