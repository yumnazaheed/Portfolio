#arrange the array in ascending order
MaxIndex=7
MyList=[7,4,5,1,3,6,2] #array list
MaxIndex=7 #number of elements
NoMoreSwaps=False #boolean to check if swap made
n=MaxIndex-1 #number of elements to compare- 0-6
Temp=0
while NoMoreSwaps== False:
    NoMoreSwaps=True
    for j in range(n):
        if MyList[j]> MyList[j+1]:
            Temp=MyList[j]
            MyList[j]=MyList[j+1]
            MyList[j+1]= Temp
            NoMoreSwaps=False
    n=n-1
print("New list is: ", MyList)
