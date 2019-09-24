'''
Created on Sep 23, 2019

@author: Admin
'''
# We use square brackets for slicing along with the index or indices to obtain a substring.
from audioop import reverse
from test.test_importlib.test_abc import abc

def stringsplit():
  
    var1 = "Guru99!"
    var2 = "Software Testing"
    print ("var1[0]:",var1[1])
    print ("var2[1:5]:",var2[0:4])
    x = "Hello World!"
    print(x[:6]) 
    print(x[0:6] + "Guru99")

test = 'guru'
#print(test[0:4])

def characterpresentornot():
    print('u' not in test)
    print('u' in test)
    print('q' in test)
    #first statement is false becuase u present in test string
    #second statement is true becuase u present in  test 
    #third will be false becuase q not present in test
#above line return true or false if r present in test string it will true else false

def stringformating():
    name = "abcd"
    number = 99
# %s %d this all arguments converted during string formatting
    print ('%s %d' % (name,number))
    #output= abcd99
# just like concat

def repeatstring():
    name = "abc"
    print(name*2)
    #output = abcabc
#print all character of string name two time like "abcabc"

def replacedata():
    olddata = "nitin tajane"
    newString = olddata.replace("tin", "tajane", 3)
    print(newString)
    #output as = nitajane tajane you can also replace full string 
 

def upercase():
    string ="automation testing"
    print(string.upper())
    return string.upper()
    
def lowercases():
    String2 = upercase()
    #here we call upercase() method to format into lower case
    print(String2.lower())
    #output = Automation or project
    
def  joinfuncationofstring():
    string1 = "project test project meeting "
    
    print(string1)
    # if you want to add a colon (:) after every character in the string "Python" you can use the following code.
    #print(":" .join('project'))
    #output = p:r:o:j:e:c:t
    
    return ":" .join(string1)
    #p:r:o:j:e:c:t: :t:e:s:t: :p:r:o:j:e:c:t: :m:e:e:t:i:n:g:
    
 
def reversestring():
    stringreverse = "testmeting"
    print(" ".join(reversed(stringreverse)))
    #output = g n i t e m t s e t

def splitStringfuncation():
    stringtestsplit = "nitni tajane sangamner"
    aftersplit =  stringtestsplit.split("j")
    print(aftersplit[0])
    #output = nitni ta
    print(aftersplit[1])
    #output = nitni ane sangamner
  
        
def stringimmutable():
    x="abc"
    x.replace("abc","xyz")
    #x= x.replace("abc","xyz")   here object create for x 
    print(x)
    
stringimmutable()   