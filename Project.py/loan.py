#this is a code for loan eligibility useful for bank 
high_income = input("Welcome please enter your bank details: ")
good_credit = input("Welcome pplease enter your bank details: ")
criminal_record = input("Welcome please enter your police report: ")

if high_income.upper()  and good_credit.upper:
    print("Eligible for loan")


elif high_income.upper() or good_credit.upper():
    print("Eligible for loan")

elif high_income.uper() and criminal_record.upper():
    print("Eligible for loan")
else:
    print("Not eligible for loan")
print("Thank you for banking with us")
 
 
