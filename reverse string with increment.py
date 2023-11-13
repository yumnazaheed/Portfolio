#print string in reverse

NewString=""
MyString=input("Enter a string: ")
num= len(MyString)-1
while num!=-1:
    NewString=NewString+MyString[num]
    num=num-1
print("New string is:", NewString)
