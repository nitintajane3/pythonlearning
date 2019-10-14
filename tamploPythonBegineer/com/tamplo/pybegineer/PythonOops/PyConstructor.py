'''
Created on Sep 26, 2019

@author: Admin
'''

class testone():
    name =""
    def  __init__(self,name):
        self.name = name
        
    def methodone(self):
        print("name  has printed " , self.name)   
        


class testtwo():
    num =0
    def __init__(self):
        self.num = 10    # if you use num instead of self.num then after run program it will give num =0
                        #self  is required in constructor  
    def methodone(self):
        print("initilise number3 is : " , self.num)    #here if you not use self.num so here program give error 
        #because self is require mention this is current instance variable other wise it will not run

if __name__ == "__main__":
    re =  testone("nitin")
    re.methodone() 
    rr = testtwo()
    rr.methodone()   #ouput is 10     