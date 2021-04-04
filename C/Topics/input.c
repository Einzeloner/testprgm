// A C program for getting input from the user

# include <stdio.h>

int main(){
    // A simple program for adding two numbers 
    float num1, num2;  // declaring two float variables

    printf("Enter the first number: ");
    scanf("%f", &num1);
    /* Explaining scanf- 'scanf' is the function that is used to take the input from the user. requires
    a character indicator like %d or %f or %s as the defining type of input and an ampersand with variable 
    like this '&variable' to know which variable to assign the input value to. */
    printf("Enter the second number: ");
    scanf("%f", &num2);
    printf("The sum of two numbers is %0.2f\n", num1 + num2);

}