#Confitional Operators 
print("Welcome to the rollercoaster")
height = int(input("Please enter the height\n"))
if height >= 120:
    print("you can ride")
else:
    print("Sorry you can't ride")

# Using %
numbercheck = int(input("please enter the number to check\n"))
if numbercheck % 2 == 0:
    print("Even")
else:
    print("Odd")

# Conditional operators 
weight = int(input("Please enter the weight\n"))
age = int(input("Please enter your age\n"))
bill = 0 
if weight > 120:
    print("you can ride")
    if age <= 18:
        bill = 7
        print("Your ticket is $7")
    elif age <= 12:
        bill = 5
        print("Yout ticket is $5")
    else:
        bill = 12
        print("Please pay $12")
        photo = input("Do you want to have a photo? If yes say y if no say n \n")
        if photo == "y":
            bill += 3 

    print(f"your final bill is ${bill}")
else:
    print("Sorry you can't ride now")
