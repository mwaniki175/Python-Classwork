def addition(P, Q):
    # This function is used for adding two numbers
    return P + Q


def subtraction(P, Q):
    # This function is used for subtracting two numbers
    return P - Q


def multiplication(P, Q):
    # This function is used for multiplying two numbers
    return P * Q


def division(P, Q):
    # This function is used for dividing two numbers
    return P / Q


# Now we will take inputs from the user
print("Please select the operation.")
print("(a). addition")
print("(b). subtraction")
print("(c). multiplication")
print("(d). division")

choice = input("Please enter choice ((a)/ (b)/ (c)/ (d)): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", addition(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", subtraction(num_1, num_2))

elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiplication(num_1, num_2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", division(num_1, num_2))
else:
    print("This is an invalid input")