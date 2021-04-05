// A C program to display conditional statements like if else, etc

# include <stdio.h>

int main(){

    int num1;
    // checking to see if even or odd
    printf("Enter a number here for cheking the condition: ");
    scanf("%d", &num1);
    int res =  num1  %  2; /* A variable for checking condition
                                                totally unneeded as the same can be in the if condition parenthesis
                                                without any problem*/
   
   /* The real condition starts here. The bracket in front of the if statement holds the condition
   for the statement to be true for.
   
   The if statement will check for the condition in parenthesis and the use the curly brackets as 
   the body for what next condition to be fulfilled.
   */ 
    if(res == 0){
        printf("%d  is even.\n", num1);
    }
    else{
        printf("%d is odd.\n", num1);
    }

    // Starting another random condition with logical operators 
    printf("Do you like onee sans [y/n]? ");
    char ans;
    scanf("%s", &ans);

    // the starting condition for a matching string
    if(ans == 'y' || ans == 'Y' || ans == 'yes' || ans == 'Yes'){       //  Or operator = ||
        printf("Ara Ara~\n");
    }
    else{
        printf("Sad onee chan noises....\n");
    }
}