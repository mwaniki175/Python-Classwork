# Inbuilt fuctions
number = max(89,70,23,45,123)
print(number)

x = min(78, 45, 34, 1)
print(x)

z = pow(2,3)
print(z)

# User-defined Functions
def name():
    print("Alexander")


name()  # Calling a function


def student():
    name = "Alexander"
    age = 17
    course = "MIT"
    print(name, age, course)


student()


# paramteres /variables and arguments /values

def students(name, age, course):
    print(name, age, course)
students("Alexander", 17,"MIT")
students("Joshua", 22,"Data Scince")
students("Noel", 19,"Cyber Security")





# User-defined function called employees then it should display details of five employees.Parameters vare as follows .fullname,age,gender,position,salary
def employees():
    fullname = "John Smith"
    age = 35
    gender = "Male"
    position = "Senior Software Engineer"
    salary = 90000
    print(fullname, age, gender, position, salary)

employees()

def employees(fullname,age,gender,position,salary):
    print(fullname, age, gender, position, salary)

employees("John Smith",35,"Male","Senior Software Engineer",90000)
employees("Emily Johnson",28,"Female","Marketing Manager",75000)
employees("David Lee",42,"Male","Sales Director",110000)
employees("Sarah Garcia",30,"Female","Human Resource Specialist",60000)
employees("Michael Mutisya",25,"Male","Financial Analyst",85000)