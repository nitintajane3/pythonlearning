'''
Created on Sep 25, 2019

@author: Admin
'''
def firstfuncation():  # def is function
    a=12
    b=13
    c=a*b     # this space is called as indentation and this is required rule of  python
    return  c
    
#print(firstfuncation())
#ouput is 156 

#declaring arguments 
def declaringargument(x,y): # this called as declaring arguments
    print(x*y) 

#declaringargument(12, 15)   #passing arguments

#To declare a default value of an argument, assign it a value at function definition

def declaringtest2(x,y=5):
    print(x*y)
    
#declaringtest2(5)    
#output = 25

def  declaringtest3(x,y=4):
    print(x*y)
    
#declaringtest2(5,y=8) 
#declaringtest2(5,8) 
#output = 40   


#You can also change the order in which the arguments can be passed in Python.

def changeorderofarguments(x,y):
    print("x value is :" ,x)
    print("y value is ", y)
    
#changeorderofarguments(y=12,x=3)  
#output = x value is 3 and y value is 12  

#Multiple Arguments can also be passed as an array

def multiplearugments(*args):
    print(args)
 
#multiplearugments(3,4,5,6,6,7,7)   
#output is (3, 4, 5, 6, 6, 7, 7)
    