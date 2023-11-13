#binary tree
#comment- global array ArrayNodes
ArrayNodes=[[0 for j in range (3)] for i in range(20)] #when declare at beginning it becomes global
#global ArrayNodes

#recursive search
def SearchValue(Root,ValueToFind):
  if Root==-1:
    return -1
  elif ArrayNodes[Root][1]==ValueToFind:
    return Root
  elif ArrayNodes[Root][1]==-1:
    return -1
  if ArrayNodes[Root][1]>ValueToFind:
    return SearchValue(ArrayNodes[Root][0],ValueToFind)
  if ArrayNodes[Root][1]<ValueToFind:
    return SearchValue(ArrayNodes[Root][2],ValueToFind)

#post order traversal 
def PostOrder(Root):
  if ArrayNodes[Root][0]!=-1:
    PostOrder(ArrayNodes[Root][0])
  if ArrayNodes[Root][2]!=-1:
    PostOrder(ArrayNodes[Root][2])
  print(ArrayNodes[Root][1]) #printing data not the position

#in order traversal
def InOrder(Root):
  if ArrayNodes[Root][0]!=-1:
    InOrder(ArrayNodes[Root][0])
  print(ArrayNodes[Root][1])
  if ArrayNodes[Root][2]!=-1:
    InOrder(ArrayNodes[Root][2])

#pre order traversal
def PreOrder(Root):
  print(ArrayNodes[Root][1])
  if ArrayNodes[Root][0]!=-1:
    InOrder(ArrayNodes[Root][0])
  if ArrayNodes[Root][2]!=-1:
    InOrder(ArrayNodes[Root][2])

#main program
for i in range(20):
  for j in range(3):
    ArrayNodes[i][j]=-1
  
Root=0
FreeNode=6

#store data in array nodes
#ArrayNodes= [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1]]
#dont hard code it like this cause then youd have to declare null pointers for the rest of the 14 elements

ArrayNodes[0][0]=1
ArrayNodes[0][1]=20
ArrayNodes[0][2]=5
#no need to declare null pointers

ArrayNodes[1][0]=2
ArrayNodes[1][1]=15

ArrayNodes[2][1]=3
ArrayNodes[2][2]=3

ArrayNodes[3][1]=9
ArrayNodes[3][2]=4

ArrayNodes[4][1]=10
ArrayNodes[5][1]=58

ValueToFind= int(input("Enter value to find: "))
Position=SearchValue(Root,ValueToFind)
print(Position)

PreOrder(Root)
