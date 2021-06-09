#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	//vars
	int num, guess, numguess = 1;

	//random number generation
	srand(time(0));
	num = rand()%100 +1; // for a number to be between 1 and 100
	
	// printf("The guessed num is %d\n", num);

	// the loop to check shit 
	
	do{
	//increment for the numguess
	numguess++;

	printf("Guess the number:");
	scanf("%d", &guess);

	if(guess < num && numguess <= 3){
	printf("This is smaller than the number.\n");
		
	}
	else if(guess > num && numguess <= 3 ){
	printf("This is larger than the number.\n");
	}
	else if(guess == num && numguess <=3){
	printf("CORRECT!\n");
	}
	else{
	printf("Out of guesses.\n");
	break;
	}
	}while(num != guess);
}	
	
