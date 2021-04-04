// A C program to have random stuff and questions thrown into it
# include <stdio.h>

 int main(){
    // Calculating area of the rectangle
    float length, breadth;
    printf("Enter the length of rectangle: ");
    scanf("%f", &length);

    printf("Enter the breadth of rectangle: ");
    scanf("%f", &breadth);
    // Answers and calculations
    printf("The area of the given rectangle would be- %0.2f\n", length * breadth);


    // calculating the area of circle
    float radius;
    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);
    // Answers and calculations
    printf("The area of the cirlce is %0.2f\n", 3.14 * radius * radius);

    // calculating the volume of cylinder with the same radius as in circle
    printf("Enter the height to calculate the area of a cylinder: ");
    float height;
    scanf("%f", &height);
    // Answer and calculations
    printf("The area of the cyllinder is %0.2f\n", (2 * 3.14 * radius * radius) + (height * 2 * 3.14 * radius));
    
   //  Now to convert the celsius into farenheit problem the OG one lmao
   printf("Enter a number to be converted into celsius from farenheit: ");
   float far;
   scanf("%f", &far);
   float cel = (far - 32) * 5/9; 
    // answers and calculation
    printf("The celsius value would be: %0.2f\n", cel);


    // A simple interest program finally 
    float years, principal, rate;

    printf("Enter the number of years: ");
    scanf("%f", &years);
    printf("Enter the principal: ");
    scanf("%f", &principal);
    printf("Enter the rate for SI: ");
    scanf("%f", &rate);
     
    // Calculating and answers
    printf("The Simple interest is %0.2f", principal * rate * years);
    return 0;
 }