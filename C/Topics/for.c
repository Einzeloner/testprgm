// A C program to understand for loops

# include <stdio.h>

void main(){
    int userinput;

    printf("Enter the number of increments: ");
    scanf ("%d", &userinput);

    // Initialize the variable , condition and instruction in the for loop all at once.

    for (int a=0; a <= userinput; a++){
        printf("Incrementation: %d\n", a);
    
    }
}