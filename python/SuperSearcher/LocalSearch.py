import os # library for os operations

def LocalSearch(User_search_request,Computer_Search_drive):
    print("currect location \n"+ os.getcwd())
    
    #Finder=input("enter search request here \n ") # the "term" the user is searching for.
    #Drive=input("which drive would you like to search? \n") # the selecter for the search location (top of file hierchy)
    result = []

    for root, dir, files in os.walk(Computer_Search_drive+":"+"/"):
        if User_search_request in files:
            result.append(os.path.join(root,User_search_request))
    print(result)
    print("\n"+"Done!")

#LocalSearch()