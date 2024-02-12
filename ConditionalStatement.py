temperature = 13

if temperature > 25:
    print("It is Hot ")
else:
    print("It is  Cold")

# A program that returns the largest number among three numbers
num1  =12
num2 = 7
num3 = 10
if num1 > num2 and num1 > num3:
    print(num1 , "is the Largest number")
elif num2 > num1 and num2 >num3:
    print(num2, "is the Largest number")
else:
    print(num3, "is the Largest number")

# A program that checks whether a number is even or odd
number = 3

if number % 2 == 0:
    print(number ,"is even")
else:
    print(number,"is odd")

# A program that checks whether a number is a prime number or not
n = 23

# A number is greater than 1
if n > 1:
    # Itterate from 2 to n/2
    for i in range (2, int(n/2)+1):
        # If n is divisible any number between 2 and n/2,it is not prime
        if (n % i) == 0:
            print(n ,"is not a prime number")
            break
    else:
        print(n ,"is a prime number")
else:
    print(n, "is not a prime number")


