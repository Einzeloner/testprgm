#include <stdio.h>
#include <math.h>

float main() {
	int num1 = 8;
	int num2 = 9;
	
	float num1f = 8.8;
	float num2f = 9.9;


	/*for printing the sum or any operation of two */
	printf("The sum (int) is  %d\n\n", num1 + num2);
	printf("The sum (float) is %f\n\n", num1f + num2f);
	printf("The mult and div (int) are %d and %d\n\n", num1 * num2, num1 / num2);
	printf("The mult and div (float) are %f and %f\n\n", num1f * num2f, num1f / num2f);

	/*now for some more functions*/
	printf("the power function for a number - %d\n\n", pow(num1, 2));
	printf("the sqrt function for a number - %f\n\n", sqrt(num1));
	
	/*ceil rounds the number to one up */
	printf("The ceil round off of the variable %f is %f\n\n ", num1f, ceil(num1f));
	/* floor rounds the number to one down */
	printf("The floor round off of the variable %f is %f\n\n ", num1f, floor(num1f));



}


