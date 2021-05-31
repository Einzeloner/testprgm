/* 
C program that accepts 4 integers p, q, r, s from the user where r and
s are positive and p is even. If q is greater than r and s is greater than p
and if the sum of r and s is greater than the sum of p and q print "Correct
values", otherwise print "Wrong values"
*/

#include <stdio.h>
#include <stdlib.h>
int main(){

	//vars
	int p, q, r, s;
	
	printf("Enter P (must be even):");
	scanf("%d", &p);
	
	printf("Enter Q (postive):");
	scanf("%d", &q);
	
	printf("Enter R(postive):");
	scanf("%d", &r);
	
	printf("Enter S:");
	scanf("%d", &s);

	// Condition checking 
	if ( p % 2 != 0 || q < 0 || r < 0){
		printf("Condition not matched. Wrong values!\n");
		exit(0);
	}
	else { 
		if ( q > r && s > p && (r + s) > (p + q)){
			printf("Condition matched. Correct values!\n");
		}
		else {
			printf("Condition matched but wrong values!\n");
		}
	}
}
