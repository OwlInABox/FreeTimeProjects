#import os # library for os operations
from LocalSearch import LocalSearch
from WebSearch import SimpleWebSearch
from SearchAnalyse import SearchReader
print("main")
User_search_request = input("please enter your search here:\n")
Computer_Search_drive = input("what drive (storage unit) to search\n")

SearchReader(User_search_request) #works
LocalSearch(User_search_request,Computer_Search_drive) #works
SimpleWebSearch(User_search_request) #works