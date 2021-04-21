// A program to find out the roots of the equation in a quadratic eq

// include section
# include <stdio.h>
# include <math.h>


void main(){
	float  a, b, c; // 3 variables for a,b,c in quad eq
	
// for the user input
	printf("Enter 'a': ");
	scanf("%f", &a);

	printf("Enter 'b': ");
	scanf("%f", &b);

	printf("Enter 'c': ");
	scanf("%f", &c);

	printf("Your equation is- %0.2fx^2 + (%0.2f)x + (%0.2f)\n", a, b, c );

	// caluclating D = b*b -4*a*c
	
	float d = (b*b) - 4*a*c;
       printf("The D of your equation is: %0.2f\n", d);
        
        // for the roots
        float root1 = (b*b - sqrt(d))/(2*a);
        float root2 = (b*b + sqrt(d))/(2*a);


       if(d < 0){
	
	      printf("The D is negetive: %0.2f\n", d);
          printf("The roots are imaginary\n");
          
  	
       }
        else if(d == 0){
            printf("The D is equal to 0\n");
            printf("The root will be the same and root will be: %0.2f\n", root1);

        }

        else{
            printf("The value of D is positive: %0.2f\n", d);
            printf("There are two roots.\n Root 1: %0.2f\n Root 2: %0.2f\n", root1, root2);

        }
        
}