'''
Created on Sep 26, 2019

@author: Admin
'''
import re
from _datetime import date

def testone():
    xx = "guru4434,education is fun"
    r1 = re.findall(r"^\d.+",xx)
    print(r1)
    today =  date.today()
    today2 = today.month
    today3 = today.year
    print(today)
    print(today2)
    print(today3)
   
    
def  reverestring():
    data = ['fdsjnfls']
    data.reverse()
    print(data)

reverestring()
 