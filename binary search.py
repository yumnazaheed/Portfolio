#binary search

#procedure
def SearchInList(SearchItem):
    Found=False
    SearchFailed=False
    First=0
    MaxItem=len(List) #dont directly use given length
    Last=MaxItem-1 #set boundaries of search area
    while not Found and not SearchFailed:
        Middle=(First+Last)//2 #find middle of current search area
        if List[Middle]==SearchItem:
            Found=True
        else:
            if Middle>=Last:#no search area left
                SearchFailed=True
            else:
                if List[Middle]>SearchItem: #must be in the first half
                    Last=Middle-1 #Move upper boundary
                else: #must be in the second half
                    First=Middle+1 #move lower boundary
    if Found==True:
        print("Found:",Middle) #output position where item is found
    else:
        print("Item is not in the array")
            

#main program

#input list
List=[9,12,33,56,73,102,455]

SearchItem= int(input("Enter item to search: "))

SearchInList(SearchItem)
