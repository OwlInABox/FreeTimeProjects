import os # library for os operations

def LocalSearch():
    print("currect location \n"+ os.getcwd())
    Finder=input("enter search request here \n ") # the "term" the user is searching for.
    Drive=input("which drive would you like to search? \n") # the selecter for the search location (top of file hierchy)

    print(os.getcwd())
    print(os.listdir())
    print(Finder)
    #print(os.walk(Drive+":"+"/"))
    #os.mkdir("OSmake")

    #search()
    #for term in Finder:

    #list
    #print(type(result))
    result = []

    for root, dir, files in os.walk(Drive+":"+"/"):
        if Finder in files:
            result.append(os.path.join(root,Finder))
    print(result)
    print("\n"+"Done!")

#LocalSearch()