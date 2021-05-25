// bank notes classification using modulus ig idk

#include <stdio.h>

int main(){
	
	// vars
	int notes;
	
	printf("Enter the amount of moni: ");
	scanf("%d", &notes);

	//500 notes
	printf("The number of 500 notes that you will have is: %d\n", notes / 500);

	//100 notes
	printf("The number of 100 notes that you will have is: %d\n", notes / 100);

	
	//50 notes
	printf("The number of 50 notes that you will have is: %d\n", notes / 50);

	//10 notes
	printf("The number of 10 notes that you will have is: %d\n", notes / 10);


}

