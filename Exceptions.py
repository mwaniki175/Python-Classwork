try:
    print(x)
except:
     print("NameError occurred")
finally:
     print("Success")



num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("ZeroDivisionError Occurred")


# User-defined Function

try:
    def multipy(x, y):
        return x * y
except:
    print("ExceptionError Occurred")

print(multipy(10, 20))
