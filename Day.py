while True:
    user_input = input("Hello! \"please enter n value\"\n")
    n = int(user_input)
    if n >= 3:
        print("Thank you! You entered:", n)
        break
    if n < 3:
        print("Please enter a bigger value\n")
    else:
        print("You must enter a number!\n")