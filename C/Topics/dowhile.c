// A C program to print natural numbers with the help of a do while loop

# include <stdio.h>

void main(){
    // variable to print till

    int num1;
    int a = 1;

    printf("The number till the series is to be printed: ");
    scanf("%d", &num1);

   do{
       printf("%d\n", a);
       a++;

   } while(a <= num1);
}
