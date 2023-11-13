import pickle
#create student binary file
def write():
    file=open("student.dat","wb")
    records=[]
    x=21
    while(x==21):
        rno=int(input("enter number "))
        name=input("enter name ")
        data=[rno,name]
        records.append(data)
        ch=input("Do you want to continue? (y/n)")
        if ch=='n':
            break
    pickle.dump(records,file)
    file.close()

def update():
    file=open("student.dat",'rb+') #opening for read and write- rb+
    s=pickle.load(file)
    final=0
    rn= int(input("enter number"))
    for i in s:
        print(rn, i[0])
        if rn==i[0]:
            print('Current number ', i[0])
            print("Current name ", i[1])

            i[0]=int(input('new number'))
            i[1]=input('new name')
            final=1
            break
    if final==0:
        print("no records found")
    else:
        file.seek(0) #making the pointer to 0th position
        pickle.dump(s,file)
    file.close()

def updateRead():
    file=open("student.dat",'rb')
    s=pickle.load(file)
    for i in s:
        print(i)
    file.close()

#main program
write()
update()
updateRead()
