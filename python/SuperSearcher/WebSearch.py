try: 
    from googlesearch import search 
except ImportError: 
    print("No module named ‘google’ found")

def SimpleWebSearch(User_search_request):
    # to search 
    query = User_search_request
    for results in search(query, tld="co.in", num=5, stop=5, pause=2): 
        print(results) 