print("hello world")

User_Input = input("please give search term: \n")
class Gsearch_python:
    def __init__(self, name_search):
        self.name = name_search
    def Gsearch(self):
        count = 0
        try:
            from googlesearch import search
        except ImportError:
            print("Module not found")
        for i in search(query=self.name,tld="com",lang="en", num=10, stop=5, pause=2):
            count += 1
            print(count)
            print(i + "\n")

if __name__== '__main__':
    gs = Gsearch_python(User_Input)
    gs.Gsearch()