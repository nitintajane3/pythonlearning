'''
Created on Oct 1, 2019

@author: Admin
'''
def testoneread():
    f= open('D:\\fileforpython\\latestfile.csv','r')
    print(f)
    for line in f:
        print(line.rstrip())
    f.close()   
    
 

def testreadwrite():
    f= open('D:\\fileforpython\\latestfile.csv','r')
    output = open('D:\\fileforpython\\outputfileteesttwp.txt','w')  # output file create automatically
    # or you can write in existing file
    for line in f:
        print(line.rstrip())
        output.write(line + '\n')
    f.close()   
    

def comparetwofile():
    f1= open('D:\\fileforpython\\comparetest1.txt','r')
    s=""
    print(f1)
    for line in f1:
        s+= line
        print(line.rstrip())
    f1.close() 
    
    f2= open('D:\\fileforpython\\comparetest2.txt','r')
    s2=""
    print(f2)
    for line2 in f2:
        s2+= line
        print(line2.rstrip())
    f2.close() 
    list1 = s.split(",");
    list2 = s2.split(",");
    print(list1)
    print(list2)
    print(len(list1))
    print(len(list2))
    
    difference = list(set(list1).difference(set(list2)))  # this is working later you can see this
    print(difference)
    
def createfile():
    new= open("D:\\fileforpython\\nitintajane123.txt",'w+')  # w is require if you want to write file
    # plus sign means if file  not exist this will  create new file 
    for i in range(10):
        new.write("This is line %d\n" % (i+1))
    new.close()
     
    
def appendfile():  
    new= open("D:\\fileforpython\\nitintajane.txt","a+")  # this a is important to append file   
    for i in range(4):
        new.write("append latest new data %d\r\n" % (i+1))
    new.close()  
    
def readfiletestsecond():
    new = open("D:\\fileforpython\\nitintajane.txt","r")
    if new.mode=="r":
        content = new.read()
        print(content)
        
readfiletestsecond()        