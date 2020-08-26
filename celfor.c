/* print the farenheit table but with for*/

#include <stdio.h>

int main()
{

int fahr;

for  (fahr = 0; fahr <= 300; fahr = fahr + 20)
printf("%3d %6.1d\n", fahr, (9*fahr)/5 + 32);
}
