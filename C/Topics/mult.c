// A C program to print the multiplication table of any n natural number

 # include <stdio.h>

 void main(){
     int fuckingnumber;

     printf("Wanna enter a number?: ");
     scanf("%d", &fuckingnumber);

    for (int a = 1; a <= 10; a++ ){
        printf("%d\n",  fuckingnumber * a);

    }     
 }