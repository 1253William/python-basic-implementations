############################################################################################################################################################################################################
##Q1.Write a python program that takes two integers as input (one per line) and prints their sum as output. For example, For the input provided as follows: 2,3 The output of the program will be: 5

  # 2 integers as input (one per line) -> accept 2 given inputs let's say x, y but each on a new line
  # since they are integers (int) -> can be +x or -x hence we want to always use as |x|
  # print their sum as output -> x + y

  # let int1 = x, and int2 = y
  # TAKE x,y
  # PARSE x,y as int and absolute
  # RETURN sum of x,y

int1 = int(input("Enter a number: "))
int2 = int(input("Enter another number: "))

total_sum = abs(int1) + abs(int2)
print("The sum of your numbers is:", total_sum)



##Q2.Write a python program that calculates the area of a rectangle, accepts inputs and displays the result
    # area of a rectangle is given as length-by-width
    # accepts inputs -> let them be l for length and w for width
    # displays the result -> l * w

    # given length as rectangle_length and width as rectangle_width
    # COMPUTE area as rectangle_length by rectangle_width
    # RETURN Area as area

rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))
area_rectangle = rectangle_length * rectangle_width
print("The area of the rectangle is:", area_rectangle)

    # A function can be written for calculating the area of this rectangle
def calc_area_rectangle():
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    total_area = l * w
    print("The area is:", total_area)

calc_area_rectangle()


##Q3.Write a python program that finds the maximum of three numbers (a, b, c) as inputs
    # finds maximum of 3 numbers given as a, b, c
    # a, b, c are inputs

    #COMPARE a = b and a = c -> a
    #COMPARE b = a and b = c -> b
    #IF not a NOR b, THEN c
    #RETURN maximum as maximum_input

#approach 1
def maximum_input(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("The maximum number is:", maximum_input(18, 32, 20))

#approach 2
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

#Compare manually
if A >= B and A >= C:
    maximum = A
elif B >= A and B >= C:
    maximum = B
else:
    maximum = C

print("The maximum number is:", maximum)



##Q4.Write a Python program that accepts a student's score (between 0 and 100) as input.
##Checks that the score is valid (must be a number between 0 and 100).
##Determines and prints the corresponding grade using this scale:
##Score Range	Grade
##90-100 A
##80-89	B
##70-79	C
##60-69	D
##Below 60	F

    # accepts score in range R = [0, 1, 2, 3, 4, 5, ...n, 100] as input
    # let input be n in range R,
    # input must be a number in range, n exists in R, if not, bounce
    # Using grade scale ( A, B, C, D , F) determine that n maps to one of these,
    # print result

    # ACCEPT n as input, n -> score
    # CHECK for n in R, if not bounce
    # MAP n to A || B || C || D || F
    # PRINT grade

score = int(input("Enter your grade ( 0 t0 100): ")) #get a score from the user

    #the score is in range
if  0 <= score <= 100:
    #determine the grade based on the score
    if score >= 90:
        grade =  'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    #print grade
    print("Your grade is:", grade)
else:
    print("Invalid score. Please enter a number between 0 and 100.")
