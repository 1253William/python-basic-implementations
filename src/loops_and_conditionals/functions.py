##Write a python program that calculates the area of a rectangle, accepts inputs and displays the result

#A rectangle's area is given as Area = Length x Width
#We don't know Area so we assign area as Area
#We accept input l and w to represent Length and Width

def calc_area_rectangle():
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    area = l  * w
    print("The area of the rectangle is: ", area)

calc_area_rectangle() #calling the defined function for execution here
