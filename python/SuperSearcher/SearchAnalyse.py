#User_search_request = input("states on search: \n")

def SearchReader(User_search_request):
    index = int(0)
    #length
    print("your input has", len(User_search_request) , "characters")

    alpha_list =[]
    symbol_list=[]
    number_list=[]

    while index < len(User_search_request):
        symbol = User_search_request[index]
        # sorting the input by type
        if str.isalpha(symbol) is False:
            if str.isdecimal(symbol) is False:
                symbol_list.append(symbol)
            else:
                number_list.append(symbol)
        else:
            alpha_list.append(symbol)

        index = index + 1

    #prints results
    print("contains:",len(number_list),"numbers")
    print("contains:",len(alpha_list),"letters")
    print("contains:",len(symbol_list),"spaces and symbols")
    print("\nDone!")

#SearchReader(User_search_request)

#SearchAnalyse()
