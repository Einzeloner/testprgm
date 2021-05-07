// A program for clalculating Ramesh's gross salary

#include <stdio.h>

int main(){
    int basic;
   
    printf("Enter your basic salary here: ");
    scanf("%d", &basic);

    printf("Your dearness allowance is: %0.2f\n", 0.4 * basic);
    printf("Your rent allowance being: %0.2f\n", 0.2 * basic);

    printf("Your gross salary being: %0.2f\n", basic + (0.4 * basic) + (0.2 * basic));
}