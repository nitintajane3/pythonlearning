'''
Created on Sep 24, 2019

@author: Admin
'''
#Various assignment operators used in Python are (+=, - = , *=, /= , etc.)



def test1():
    num1 = 4
    num2 = 5
    print(("Line 1 - Value of num1 : ", num1))
    print(("Line 2 - Value of num2 : ", num2))
 
    
def test2():
    num1 = 4
    num2 = 5
    res = num1 + num2
    res += num1
    print(("Line 1 - Result of + is ", res))  
    # output == ('Line 1 - Result of + is ', 13)  
    
def test3():
    a = 12
    b=14
    c=a+b
    print(c)
    z=c/a 
    print(z)  
    #output = 26 and 2.1666 

def test4():
    a = 12
    b=14
    c=a+b
    print(c)
    c/=a  #if you remove = sign you then your divide not work show error, you need variable to store it 
    c+=a
    print(c)  
    #output = 26 and 14.1666
    
def findoutdatatypeofvariable():
    a= False
    print("%s" %type(a)) #you need %s to display type of variable 
    #print("%d" %type(a))  >> you get error as "a number is required, not type  "
    #print("" %type(a))  >> you get error as "not all arguments converted during string formatting"
    #print("%z" %type(a)) >>> you error as "unsupported format character 'z'"
    
    #output = <class 'bool'> 
    
def logicaloperator():
    a=True
    b=False
    print(a and b)
    print(not a)  #output is false because a is true 
    print(not b)   #output is true because b is already false condition false 
    #here we are checking b is false or not so output is false if b true then it will return true
    p = 4
    q= 4
    print(p >3 or q<3)
    
    
def membershipoperator():
    a=21
    b=4
    list=[1,2,4,3,5,6,7,8];
    if a in list :
        print(a, "  this number  present in list")
    else :
        print(a, "  this number not present in list")


#To compare the memory location of two objects, Identity Operators are used. The two identify operators used in Python are (is, is not).

def identityoperator():
    x = 30
    y = 20
    if ( x is y ): 
        print("x & y  SAME identity")
   
    y=30
    if ( x is not y ):
        print("x & y have DIFFERENT identity") 
    
        
identityoperator()        