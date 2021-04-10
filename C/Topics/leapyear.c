// A C program to determine  if the user has given us a leap year

#include <stdio.h>

void main(){
    int inputyear;
    printf("Enter the year: ");
    scanf("%d", &inputyear);

    if(inputyear % 4 == 0){
        printf("Yes. The year %d is a leap year\n", inputyear);
    }

    else{
        printf("No. The year %d is not a leap year.\n", inputyear);
    }

}