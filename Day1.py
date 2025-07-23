# Variables
x = 5
y = "Hassaan"


# Datatypes
"""
1)int
2)float
3)str
3)bool
4)dict
5)list
6)tuple
7)set"""
basic_int = 5                       #int
print(basic_int)

basic_str = "5"                     #string
print(basic_str)

basic_float = 5.5                     #float
print(basic_float)

basic_bool = True                    #bool
print(basic_bool)

basic_dict = {"Key": "Value"}        #dict
print(basic_dict["Key"])

basic_list = [1, 2, 3, 4, 5]         #list
print(basic_list[0])
basic_list.insert(4,5)
print(basic_list)


basic_tuple = (1, 2, 3, 4)            #tuple
print(basic_tuple[0])
#Note: Tuples are immutable, so you can't append, remove, or change values.


# #String Manipulation

s = "Hello World"
print(len(s))
print(s.lower())
print(s.upper())
print(s.title())
print(s.replace("World", "Python"))


# # Operators
"""
1)Arithmatic(+, -, *, /)
2)Comparison(==, =!, >, <)
3)Logical(and, or, not)
4)Assignment(=, +=, -=)
"""
operator_ = 5
operator_ += 10
print(operator_)


# #String Slicing
s = "Python"
print(s[0:2])
print(s[:4])
print(s[-4:2])
print(s[-1])


# #Conditional Statements

age = int(input("Enter your age: "))
if age == 18:
    print("You are an adult")
elif age > 5:
    print("You are greater than 18")
else:
    print("You are not an adult")

# #Ternary Operator
age = input("Enter age: ")
status = "Adult" if age>= "18" else "Minor"
print(status)

#Loops

#for loop
numbers = int(input("Enter the numbers you want to print: "))
for i in range(numbers):
    print(i)

# While Loop
i = 0
while i< 5:
    print(i)
    i += 1


# Break
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# Functions
def meet(name):
    return f"Hello {name}"
print(meet(input("Enter your name: ").title()))



