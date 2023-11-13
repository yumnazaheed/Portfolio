#read from file and paste into new file

#read from StudentDetails

fh=open('StudentAverage.txt','w')
def ReadFile():
    MyFile= open('StudentDetails.txt','r')
    for line in MyFile:
        line=line.strip('\n')
        Details=line.split(',')
        Average=CalAverage(Details) #seperate functions
        WriteAverage(Details,Average)
    MyFile.close()

#Calculate the average
def CalAverage(Details):
    Average=0 # i in range( starting- inclusive, ending-exclusive)
    for i in range(2,5):#totalling marks- directly access
        Average=Average+ int(Details[i])
    Average=Average/4
    return Average

#write to new file
def WriteAverage(Details,Average):#write to new file
    OutputLine=Details[0]+ "," + Details[1]+ "," + str(Average)
    fh.write(OutputLine+"\n") #include line break

    
#main program
ReadFile()
fh.close()
