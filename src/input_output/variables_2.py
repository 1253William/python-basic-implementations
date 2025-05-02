##In python you can assign multiple values to variables

x, y, z = 1, 5, 20
##the values/data are assigned respectively to their variables in index
veg1, veg2, veg3 = "Onion", "Cucumber", "Carrot"

#if the number of values does not match the number of variables python throw an error
# car1, car2, car3 = "Volvo", "GLE"  ##Not enough values

fruits = ["Mango", "Banana", "Apple"]
##unpacking a collection
fruits1, fruits2, fruits3 = fruits

print(x, y, z)
print(veg1, veg2, veg3)
# print(car1, car2)
print(fruits1, fruits3, fruits1)

##Global variables - variables that are outside a function and accessible anywhere inside and outside a given function
##You can use a global keyword to make a local variable global in state
expression = "awesome" ##variable expression is created outside the function greet() but it is being used in the block

def greet():
    user = input("Enter your name: ")
    print(f'Good day, {user} I feel   { expression }  today')

greet() #you call the function here, do not print()

def greet2():
    global expression
    expression = "great"
    user = input("Enter your name: ")
    print(f'Good day, {user} I feel   { expression }  today')

greet2()