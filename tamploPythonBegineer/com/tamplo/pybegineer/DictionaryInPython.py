'''
Created on Sep 24, 2019

@author: Admin
'''
def dictionaryfirsttest():
    Dict = {'Tim': 18,'Charlie':23,'Tiffany':22,'Robert':25}    
    print (Dict['Charlie'])
    

def copydirectory():
    boys = {'nitin':12,'vikrant':13,'sameer':14};
    girls ={'ekta':15,'poonam':17};
    boysall = boys.copy();
    girlsall = girls.copy();
    print(boysall)
    print(girlsall)
    #update directory
    boys.update({'ashtosh':10})
    print(boys)
    #boys.__delitem__('sameer')
    del boys ['nitin']
    print(boys)
    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25} 
    print ("Students Name: %s" % Dict.items())
    
def searchkeyindirectory():
    Dict = {'Tim': 18,'Charlie':23,'nitin':12,'vikrant':13,'sameer':14} 
    boys = {'nitin':12,'vikrant':13,'sameer':14};
    for key in list(Dict.keys()) :
        if key in list(boys.keys()):
            print(True)
        else :
            print(False)


def sortingdatatest1():
    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}   
    for S in Dict:
        print(S)
        #output = Tim Charlie Tiffany Robert this all name display separate each line 


dict = {'nitin':10,'tajane':11,'vijendra':4,'sangamner':15,'asha':19}   

def sortingdatatest2():
   
    alldata = list(dict.items())
    alldata.sort() 
    for s in alldata:
        print(s)
        #output = ('asha', 19)     ('nitin', 10)    ('sangamner', 15)   ('tajane', 11)   ('vijendra', 4)


def lengthofdirectory():
    print(len(dict))
    print("Length : %d" % len (dict))
    
def knowvariabletype():
    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
    r = 12    
    print("variable Type: %s" %type (r))
    #output = variable Type: <class 'int'>
    
def makedirectoryintoprintableformat():
    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}    
    print("printable string:%s" % str (Dict))    
    #  output = printable string:{'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25} 
    
makedirectoryintoprintableformat()    