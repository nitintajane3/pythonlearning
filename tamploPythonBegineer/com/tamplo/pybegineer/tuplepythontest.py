'''
Created on Sep 24, 2019

@author: Admin
'''
def tupletest():
   
    tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
    tup2 = (1,2,3,4,5,6,7);
    print(tup1[0])
    print(tup2[1:4])
    nitin = ('nitin','tajane','sangamner','tajane mala','6 th jan 1992');
    print(nitin[2])
    
def packingAndUnpackingtest():
    userdetails = ('nitin tajane','6th jan 1992','automation tester','4 year experience');
    (name,birthday,profile,yearofexperience) = userdetails
    print(name)
    print(userdetails[0:4])
    
def comparingtupletest():
    a=(4,5)  #here comparing first one then second number of both tuple 
    b=(3,9)  #if first number of both tuple are same then they search for second number of both tuple
    # generate result if first two number are not same of two tuple
    if(a>b):print("a is grether than b")
    elif (a==b) : print("a and be are  equal")
    else : print("a is less than b")
      
def keydirectorytest():
    a={'x':100,'y':200}
    b= list(a.items())
    print(b)
     
keydirectorytest()    
       
    
        