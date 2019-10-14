'''
Created on Oct 1, 2019

@author: Admin
'''


import pathlib
from os import path
import shutil
import time
import urllib.request

def testone():
    
    print("file exist:"+str(path.exists('D:\\fileforpython\\nitintajane.txt')))
    print("File exists:" + str(path.exists('D:\\fileforpython\\nitintajan34334e.txt')))
    print("directory exists:" + str(path.exists('D:\\fileforpython')))

def testtwo():
    
    print("file exist:"+str(path.isfile('D:\\fileforpython\\nitintajane.txt')))
    print("File exists:" + str(path.isfile('D:\\fileforpython\\nitintajan34334e.txt')))
    print("directory exists:" + str(path.isfile('D:\\fileforpython')))
    

def pathlibtest():
    file = pathlib.Path("D:\\fileforpython\\nitintajane.txt")
    if(file.exists()):
        print("file exist")
    else:
        print("file not exist")
        
def getcurrentfilepath():
    if path.exists("D:\\salary slips\\Salary Slip_Nitin Tajane.xlsx"):
        src = path.realpath("nitintajane.txt")  
        #  here src variable print the current eclipse directory 
        head,tail = path.split(src)
        print(head)
        print(tail)
        

def createcopy():
    file = pathlib.Path("D:\\fileforpython\\nitintajane.txt")
    if(file.exists()):
        src = path.realpath("D:\\fileforpython\\nitintajane.txt")
        print(src)
        dst = src + ".txt"  # if we not add this ".txt it will  give error for duplicate file "
        shutil.copy(src, dst)
        print(src)
        # above path new one file created with name is nitintajane.txt.bk
        
        #copy over the permissions,modification
        shutil.copystat(src,dst)

def getlastmodfificationdetails():
    t = time.ctime(path.getmtime("D:\\fileforpython\\nitintajane.txt"))
    print(t)
    

def redirecttourl():
    # open a connection to a URL using urllib2
    webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')
  
    #get the result code and print it
    print ("result code: " + str(webUrl.getcode()) )
  
    # read the data from the URL and print it
    data = webUrl.read()
    print (data)
    
redirecttourl()    