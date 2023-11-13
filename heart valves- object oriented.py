class Heart:
    def __init__(self, heartValves):
        self.heartValves= heartValves

    def displaying(self):
        return self.heartValves

class Person:
    def __init__(self, fname, lname, address, heartValves):
        self.__fname= fname
        self.__lname= lname
        self.__address= address
        self.__heartValves= heartValves
        self.__heartObject= Heart(self.__heartValves) #composition
        #creating an instance
        #self.__heartObject- this is an object

    def display(self):
        print("First Name: ", self.__fname)
        print("Last Name: ", self.__lname)
        print("Address: ", self.__address)
        print("No of Heart Valves: ", self.__heartObject.displaying())

p= Person("Adam","syn","876 zyx Ln", 4)
p.display() #.display() because defined in class
