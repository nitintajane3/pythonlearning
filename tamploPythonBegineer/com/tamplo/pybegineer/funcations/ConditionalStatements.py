'''
Created on Sep 25, 2019

@author: Admin
'''


def conditiontest1():
    x,y = 6,4
    if(x<y):
        st="x is bigger"
    print(st)
    
#output = it will show error because x is not small than y  and if condition not true and  we never declare st is other condition
#means did not mention or handle condition for if statement false   
#local variable 'st' referenced before assignment
#if __name__=="__main__":
    #conditiontest1()
    

def conditiontest3():
    x,y=12,5
    if (x<y):
        print("x is less than y")
    
#conditiontest3()     
#here condition not closed so if condition false nothing to display so after run progress nothing to display
#print statement we keep below to if statement but not at same line see above example    
    


#If one condition goes wrong, then there should be another condition that should justify the statement or logic.
def conditiontest4():
    x,y =8,4
    if(x < y):
        st= "x is less than y"
    else:
        st= "x is greater than y"
    print (st)
    
#conditiontest4()
#output = x is greater than y    

def conditiontest5():
    x,y=10,9
    if(x<y):
        print("x is  less than y")
    elif(x==y):
        print("x and y are equal")
    else:
        print("x is grather than y")
    

#this is  for  minimal  statement     
def conditiontest6():
    x,y = 8,8
    str = "meeting" if(x<y) else "tajane"
    print(str)
    
#conditiontest6() 

def nestedifelsecondition():
    country =  "IND"
    x,y = 9,10
    if(country =="IND"):
        if(x > y):
            print("x is greter than y and county is IND")
        elif(x == y):
            print("x and y are equal and country is IND")  
        else:
            print("x is less than y and country is IND")    
        
    elif(country=="AU"):
        if(x > y):
            print("x is greter than y and county is AU")
        elif(x == y):
            print("x and y are equal and country is AU")  
        else:
            print("x is less than y and country is Au")     
    else:
            print("country not listed")
           
#nestedifelsecondition()

#python does not support switch statement but Python uses dictionary mapping to implement switch statement in Python
def switchstatement(argument):
    direct = {
        0: "nitin tajane",
        1: "vikraant golhr",
        2: "poonam ",
        3: "ashtsh",
        4: "sayali",
    }
    return direct.get(argument, "nothing key not  match")

  
    
def SwitchExample():
    Dict = {'Tim': 18,'Charlie':23,'Tiffany':22,'Robert':25}    
    alldata = list(Dict.items())
    print(alldata)
  
#while loop
def whileloopfirstprogream():
    x=0
    while(x<8):
        print("x is print",x)
        x = x+1;
        
#whileloopfirstprogream()  


#for loop
def forloopfirstprogream():
    for x in range(0,5):
        print(x)           
        
#forloopfirstprogream()

def forloopinmonth():
    months =["Jan","Feb","Mar","April","May","June"] 
    for m  in months:
        print(m)    
        
#forloopinmonth()   

def breakandcontinue():
    for x in range (10,20):
            #if (x == 15): break      #10,11,12,13,14
            if (x % 2 == 0) : continue  #11,13,15,17,19
            print(x)
                    
#breakandcontinue()   

def enumutora():
    Months = ["Jan","Feb","Mar","April","May","June"]
    for i, m in enumerate (Months):
        print(i,m)    
        
enumutora()
#output = 
#0 Jan
#1 Feb
#2 Mar
#3 April
#4 May
#5 June
                                   