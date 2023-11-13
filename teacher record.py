
import pickle
def addrecord():
    f=open("teacher.dat",'wb') #dat files are in computer readable form
    d=[]
    ch='y'
    while ch=='y':
        tname=input('enter teacher name ')
        tdesignation=input('enter designation ')
        tsal=float(input('etner teacher salary'))
        temp=(tname, tdesignation,tsal)
        d.append(temp)
        ch=input('do you want to continue y or n')
    pickle.dump(d,f) #append whole array all together
    f.close()
    
def bread(): #cant directly read- read binary 
    f=open("teacher.dat","rb") #rb= read binary
    d= pickle.load(f) # load to read from file like GETRECORD
    for i in d: #d has an array of records- i addresses each element
        print(i)#prints data from dat file
    f.close()
    return d

def Search(d):
    SearchValue=input("enter name: ")
    for i in d:
        if i[0]==SearchValue: #dont split element with ','
            #if it gives you a tuple error it means its already
            #an array so dont split at ','. you can just reference elements
            #using indexing e.g. i[0]
            print(i)

addrecord()
d=bread()
Search(d)
