user_data = int(input("Enter a number: "))

isHappy = False

if not isHappy or user_data == 6: # or | and
    print("Unhappy")
elif user_data == 5:
    print("Number is 5")
else:
    print("Happy")

number = 5 if user_data == 5 else 0
print(number)

# if user_data > 5:
#     print("number is bigger than 5")
#     if user_data > 10:
#         print("number is smaller than 10")
#     print("LOL")
