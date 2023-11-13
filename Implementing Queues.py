Queue=["" for i in range (10)]
def InitialiseQueue ():
    global RearPointer,FrontPointer,Queue,NumberInQueue,MaxQueueSize
    MaxQueueSize=10
    NumberInQueue=0
    RearPointer=-1
    FrontPointer=0
    
    

def AddItem(Data):
    global RearPointer,FrontPointer,Queue,NumberInQueue,MaxQueueSize
    if NumberInQueue==MaxQueueSize:
        return False
    else:
        if RearPointer>=-1:
            if RearPointer==MaxQueueSize:
                RearPointer=-1
            RearPointer=RearPointer+1
            Queue[RearPointer]=Data
            NumberInQueue=NumberInQueue+1
            return True

def DeleteItem():
    global RearPointer,FrontPointer,Queue,NumberInQueue,MaxQueueSize
    if NumberInQueue==0:
        return False
    else:
        if FrontPointer==MaxQueueSize:
            FrontPointer=0
        Queue[FrontPointer]=""
        FrontPointer=FrontPointer+1
        NumberInQueue=NumberInQueue-1
        return True
    
InitialiseQueue()
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(AddItem("A"))
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(DeleteItem())
print(Queue)
            
            
         
    
