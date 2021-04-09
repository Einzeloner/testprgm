// Another condtional program to check and display income tax

/* condition given
       income slab                Tax
        2.5l - 5.0l                     5%
        5.0l - 10.0l                  20%
        Above 10l                    30%
        no tax below 2.5l
*/

# include <stdio.h>

void main(){
    float  income;

   printf("Enter your annual income: ");
   scanf("%f", &income);
    
    if (income <= 250000){
        printf("Your income tax will be: 0\n");
    }
    else if (income >= 250000 && income <= 500000){
        printf("Your income tax would be: %0.2f\n", income * 0.05);
    }
    else if (income >= 500000 && income <= 1000000){
        printf("Your income tax would be: %0.2f\n", income * 0.2);
    }
    else if(income >= 1000000){
         printf("Your income tax will be: %0.2f\n", income * 0.3);
    }
    else{
        printf("Invalid input\n");
    }

}