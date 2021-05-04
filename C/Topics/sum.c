// A C program to calculate the sum of natural numbers
# include <stdio.h>

void main(){
    int  i = 0, n = 0, numlimit;

    printf("Enter the range till which the number is to be added: ");
    scanf("%d", &numlimit);

    for (i;  i <= numlimit ; i++){
    n += i;
    printf("Sum = %d\n", n);       
    }
}