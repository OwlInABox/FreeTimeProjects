from LocalSearch import LocalSearch
from WebSearch import SimpleWebSearch
from SearchAnalyse import SearchReader
#print("main")
def run():
    while True:
        User_search_request = input("please enter your search here:\n")
        if len(User_search_request) <=0:
            print("no input given")
            break

        Computer_Search_drive = input("what drive (such as 'c') to search\n")
        if len(Computer_Search_drive) > 1:
            print("Error, only one single letter can be used for drive")
            break
        if str.isalpha(Computer_Search_drive) is False:
            print("Error, input is not the letter of a drive.")
            break


        SearchReader(User_search_request) #works
        LocalSearch(User_search_request,Computer_Search_drive) #works maybe needs to be less specefic
        SimpleWebSearch(User_search_request) #works
        break

    the_end = input("restart? y / n")
    if the_end == "y":
        run()
    else:
        pass
run()