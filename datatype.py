# data Types
number = 45 # int
num = 56.78 # float
greeting = "Hello there " # str
IsPythonInteresting = True # bool

# variable storing multiple values
Languages = ["Python" , "php" , "java"] # list
fruits = ("Apple","Banana","Pineapple") # tuple
countries  = {"Kenya", "China","USA"} # set
# dictionary
details = {
    "firstname" : "Grace" ,
    "age" : 17 ,
    "course" : "MIT" ,
    "nationality" : "North America"
}
print(number)
print(greeting)
print(countries)
print(IsPythonInteresting)
print(details)
print(details["course"])
print(details["nationality"])

# determining the data type
print(type(details))
print(type(countries))

# type casting--converting one data type to another
print(float(number))
print(int(num))