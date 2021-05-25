// A C program to calculate distance between two 2d points

#include <stdio.h>
#include <math.h>

int main(){

	int x1, y1, x2, y2;
	
	printf("Enter x1: ");
	scanf("%d", &x1);

	printf("Enter x2: ");
	scanf("%d", &x2);

	printf("Enter y1: ");
	scanf("%d", &y1);

	printf("Enter y2: ");
	scanf("%d", &y2);

	float dist = (x2 - x1) * (x2 - x1) - (y2 - y1) * (y2 - y1);


	printf("The distance between the two points is: %0.2f\n", sqrt(dist));


}
