//  using else if and else if clauses with one liners switch cases and conditional operators

// A program to find the grade of the sutdent  based on their marks

#include <stdio.h>

void main(){
    float  math, phy, chem, english, misc;
   // 5 variables for their marks in the respective sub

    printf("Enter marks in Maths: ");
    scanf("%f", &math);
    
    printf("Enter marks in Physics: ");
    scanf("%f", &phy);
   
    printf("Enter marks in Chemistry: ");
    scanf("%f", &chem);
  
    printf("Enter marks in English: ");
    scanf("%f", &english);
 
    printf("Enter marks in Misc: ");
    scanf("%f", &misc);

   // Now for the result display with the help of switch statement 
   float res =( (math + phy + english + chem + misc)/500) * 100 
   // full marks being 100 in one subj. This will be used to calculate the percentage 
    
}

