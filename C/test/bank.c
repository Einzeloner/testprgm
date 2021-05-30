// bank notes classification idk 

#include <stdio.h>

int main(){ // Talking to me is like talking to a brick
	
	// vars
	int amt, total;
	
	printf("Enter the amount of moni: ");
	scanf("%d", &amt);

	//500 notes
	total = (int)amt / 500;
	printf(" The 500 rs notes are: %d\n", total);
	
	amt = amt - (total * 500);
	
	//100 notes
	total = (int)amt / 100;
	printf(" The 100 rs notes are: %d\n", total);
	
	amt = amt - (total * 100);
	
		
	//50 notes
	total = (int)amt / 50;
	printf(" The 50 rs notes are: %d\n", total);
	
	amt = amt - (total * 50);

	//10 notes
	total = (int)amt / 10;
	printf(" The 10 rs notes are: %d\n", total);
	
	amt = amt - (total * 10);
}

