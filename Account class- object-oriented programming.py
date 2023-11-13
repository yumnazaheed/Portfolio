#Account class
class Account():
    def __init__(self, AccountNumber, Balance):
        self.__AccountNumber=AccountNumber
        self.__Balance=Balance
    #getters
    def getAccountNumber(self):
        return self.__AccountNumber
    def getBalance(self):
        return self.__Balance
    #setters
    def setAccountNumber(self, AccountNumber):
        self.__AccountNumber=AcountNumber
    def setBalance(self, Balance):
        self.__Balance=Balance
    
#Current Account class
class CurrentAccount():
    def __init__(self, Level, Fee):
        self.__Level=Level
        self.__Fee=Fee

    #getters
    def getLevel(self):
        return self.__Level
    def getFee(self):
        return self.__Fee

    #setters
    def setLevel(self, Level):
        self.__Level=Level
    def setFee(self, Fee):
        self.__Fee=Fee

#declare savings account class
class SavingsAccount():
    def __init__(self):
        self.__RegularAmount=0.0
        self.__PaymentInterval=0
