#code for insertion sorting

def InsertionSort(MyList,NumberOfItems):
    ItemToBeInserted=0
    CurrentItem=0
    
    for Pointer in range(NumberOfItems):
        ItemToBeInserted=MyList[Pointer]
        CurrentItem=Pointer-1 #pointer to last item in the sorted part of the list

        while(MyList[CurrentItem]>ItemToBeInserted and CurrentItem>-1):
            MyList[CurrentItem+1]=MyList[CurrentItem] #move current item down
            CurrentItem=CurrentItem-1 #look at item above
        MyList[CurrentItem+1]=ItemToBeInserted #Insert item
    print("Sorted list",MyList)


#main program
NumberOfItems=0
MyList=[]
Number=int(input("Enter numbers to sort, enter 000 to end input: "))
while Number!= 000:
    MyList.append(Number)
    NumberOfItems=NumberOfItems+1
    Number=int(input("Enter numbers to sort, enter 000 to end input: "))
print("original list",MyList)

InsertionSort(MyList, NumberOfItems)
