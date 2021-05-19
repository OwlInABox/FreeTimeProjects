#include <iostream>
#include<cstdlib>

int DiceResult()
    {
        std::cout << "how  many dice do you want to roll? \n";
        int x;
        std::cin >> x;
        
        for (int i =0; i < x;  i++ ) 
            {
                int roll =rand() % 6 +1;
                std::cout << roll << "\n";
            }

        return 0;
    }


int main(int argc, char* argv[])
    {
        //std::cout << "hello world!";

        DiceResult();
        return 0;
    }
