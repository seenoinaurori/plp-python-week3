# bug_hunt.py

# BUG: The opening print statement was missing the closing quotation mark.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: The program printed the text "nmae" instead of using the variable name.
print("Nice to meet you,", name)

age = int(input("How old are you? "))

# BUG: Age was stored as text, so adding 1 caused an error.
# Converting age to an integer allows correct arithmetic.
print("Next year you will be", age + 1)
