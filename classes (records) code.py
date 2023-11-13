class StuRecord: #Declaring a class without other methods
    def __init__(Student): #constructor #LEAVE A SPACE
        Student.name=""
        Student.Mark1=0
        Student.Mark2=0

Student=[StuRecord() for i in range(8)] #create an array of records type StuRecord
#Enter data
for i in range(2):
    Student[i].Name=input("Enter Student name: ")
    Student[i].Mark1=int(input("Enter mark 1: "))
    Student[i].Mark2=int(input("Enter mark 2: "))
#output
for i in range(2):
    print(Student[i].Name)
    print(Student[i].Mark1)
    print(Student[i].Mark2)
