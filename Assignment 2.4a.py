# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:40:10 2018

@author: zabiulla.khan

Write a Python Program(with class concepts) to find the area of the triangle using the
below formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the
parent class and function to calculate the area should be defined in subclass.

"""

class Length:
    # Length class accepts no_of_sides parameter
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # self.sides is a list to store values of n sides
        self.sides = [0 for i in range(no_of_sides)]

    # Accepts sides from user
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # Displays sides accepted from user
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

       
class Area(Length):
    def __init__(self):
        # Invokes parent class with no_of_sides arg as 3
        Length.__init__(self,3)

    def findArea(self):
        #assigns the local variables a,b,c with the sides recieved from parent class
        a, b, c = self.sides
        
        # calculates the semi-perimeter
        s = (a + b + c) / 2
        
        # calculates the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        
        #rounds off the area value upto 2 decimal values
        print('The area of the triangle is %0.2f' %area)
        
# instantiate the Sub class
area1= Area()
# Get the lengths from parent class
area1.inputSides()
# display the lengths from parent class
area1.dispSides()
# calculate and display  the area from sub class
area1.findArea()



