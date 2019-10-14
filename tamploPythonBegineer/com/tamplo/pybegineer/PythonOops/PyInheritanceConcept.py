'''
Created on Sep 26, 2019

@author: Admin
'''
from com.tamplo.pybegineer.PythonOops.PyClasses import ityss
class ityss2():
    def vikrant(self,test):
        print("vikrant in ityss",test)
    def sayali(self):
        print("sayali in ityss")

class bics(ityss2):
    def nitin(self):
        print("nitin method execute ")
        c = ityss()   # here we called to other class of python shell script 
        c.vikrant()    #  and here we called method of ityss class 


#self is first parameter of instance methods      
#The self-argument refers to the object itself  


class poonam():
    def test1(self):
        print("poonam test 1 method")


class derivedclass(poonam):
    def test1(self):   #override method of poonam class
        print("derived classs,  test1 method")
        poonam.test1(self)
 
class derived2class():
    def test1(self):   #override method of poonam class
        print("derived 2 classs,  test1 method")
        poonam.test1(self)    #if you are calling method using class name you need self argument 
        q =bics()
        q.sayali()
        # above code does not required self argument in method calling because object is created
        bics.sayali(self)  
        #above code self is require because object not created you directly calling by class name




#if __name__ == "__main__":
    #p = bics()   #here we create object of bics class 
    #p.nitin()     # here we create nitin method 
    #a = ityss2()   # here we create object of ityss2 
    #a.vikrant("test")   #here we call to vikrant method from  ityss2 class  
    
w = derivedclass()
w.test1()   
w = derived2class()
w.test1()    