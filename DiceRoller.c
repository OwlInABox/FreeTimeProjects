#include <stdio.h>
#include <stdlib.h>

int main()
	{
		printf("spider,online! \n \n");
		printf("what functions should be added? \n");
		int data = 16;
		printf("%x\n",data);

		printf("enter the number of dice\n");
		int dice, rolls, sides;
		scanf("%d", &dice);
		printf("side number\n");
		scanf("%d", &sides);
		printf("the results are: \n");

		for (rolls =0; rolls < dice; rolls++)
			printf("%d \n",(rand()% sides) +1 );
		printf("\n");
		return 0;
	}
