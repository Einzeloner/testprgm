// A C program to understand for loops

# include <stdio.h>

void main(){
    int userinput;

    printf("Enter the number of increments: ");
    scanf ("%d", &userinput);
      
      for (int i = userinput; i; --i){
          printf("%d\n", i);
      }
}