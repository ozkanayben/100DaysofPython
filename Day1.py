# Demonstration of basic Python functions: print(), input(), len()

# Example 1: Using print()
print("Hello!\nHello!")

# Example 2: Using input() and string concatenation
name = input("What is your name? ")
print("Hello, " + name + "!")

# Example 3: Using len() directly
print("Your name has " + str(len(input("What is your name? "))) + " characters.")

# Example 4: Using input() and len() in a cleaner way
username = input("Can I have your name? ")
length = len(username)
print("Your name is " + str(length) + " characters long.")
