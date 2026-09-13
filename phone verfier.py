phone_number = input("Please enter your phone number : ")
length = len(phone_number)
result = 0
if length > 10 :
    print("A phone number must be 10 digits long")
elif length < 10 :
    print("A phone number must be 10 digits long")
else :
    result = phone_number.isdigit()

if result is True:
    print(f"Your phone number +91{phone_number} has been registered with us!")
elif result is False and length ==10:
    print("Kindly input a valid phone number")    