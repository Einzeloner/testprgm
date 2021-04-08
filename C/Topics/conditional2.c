// program to find out the grade of the student 
#include <stdio.h>

void main(){
    // declaring variable for the three subs
    int maths, phy, chem;

    printf("Enter marks for Maths: ");
    scanf("%d", &maths);
    
    printf("Enter marks for Physics: ");
    scanf("%d", &phy);
    
    printf("Enter marks for  Chemistry: ");
    scanf("%d", &chem);

    
    // a result variable 
    int resc = (maths + chem + chem) *100 / 300 ;
    // printf("Your result is: %d\n", resc);


    // now for the chekcing below 33% part assuming full marks to be 100
    if (maths <= 33 || phy <= 33 || chem <= 33 || resc <= 40){
        printf("You have scored less than 33 or less than 40 percent in one or more subs.\n Thus you are fail. \n");
        printf("Your result is: %d\n", resc);
        
    }
    
    else{
        printf("You scored %d percent\n", resc);
    }


}


