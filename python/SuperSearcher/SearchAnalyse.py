print("Blues and jazz")
User_input = input("states on search: \n")
class SearchAnalyse():
    def SearchReader():
        index = int(0)
        #length
        print("your input has", len(User_input) , "characters")

        alpha_list =[]
        symbol_list=[]
        number_list=[]

        while index < len(User_input):
            symbol = User_input[index]
            #print(type(symbol))
            if str.isalpha(symbol) is False:
                if str.isdecimal(symbol) is False:
                    symbol_list.append(symbol)
                else:
                    number_list.append(symbol)
            else:
                alpha_list.append(symbol)

            index = index + 1

        
        print("contains:",len(number_list),"numbers")
        print("contains:",len(alpha_list),"letters")
        print("contains:",len(symbol_list),"spaces and symbols")

    SearchReader()
    print("\ndone!")
SearchAnalyse()
