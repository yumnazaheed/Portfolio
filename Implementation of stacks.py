Stack=["" for i in range (10)]

def InitialiseStack():
    global TopOfStackPointer
    global Stack
    BasePointer=0
    TopOfStackPointer=-1
    

def AddItem(Data):
    global TopOfStackPointer
    global Stack
    if TopOfStackPointer==len(Stack):
        return False
    else:
        TopOfStackPointer =TopOfStackPointer+1
        Stack[TopOfStackPointer]=Data
        return True 
        
def DeleteItem ():
    global TopOfStackPointer
    global Stack
    print (TopOfStackPointer)
    if TopOfStackPointer==-1:
        return False
    else:
        Item=Stack[TopOfStackPointer]
        TopOfStackPointer=TopOfStackPointer-1
        return Item 
InitialiseStack()    
AddItem("A")
AddItem("B")
print (TopOfStackPointer)
print(DeleteItem())
AddItem("C")
print(Stack)
        
