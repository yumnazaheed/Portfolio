#DECLARE MaxIndex, i, j :INTEGER
#DECLARE NoMoreSwaps:BOOLEAN
Result=[1,98],[2,67],[3,87],[4,90],[5,76]

def Sort():
    MaxIndex=4
    NoMoreSwaps=False
    while NoMoreSwaps==False:
        NoMoreSwaps=True
        for i in range(MaxIndex):
            if Result[i][1]>Result[i+1][1]:
                for j in range(2):
                    ExamResult=Result[i][j]
                    Result[i][j]=Result[i+1][j]
                    Result[i+1][j]=ExamResult
                NoMoreSwaps=False
        MaxIndex=MaxIndex-1
    print(Result)        
#main program
Sort()

