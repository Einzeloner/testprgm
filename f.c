#include <stdio.h>
/* ehh some random table about temparatures */


float main() {
{
printf("Temp table\n");
}
float fahr, celsius;
float lower, upper, step;

lower = 0;		/* lower limit of the scale*/
upper = 300;		/* upper limit of the scale*/
step = 20;		/* pretty self explanatory*/

fahr = lower;
while (fahr <= upper) {
celsius = (5.0/9.0) * (fahr-32.0);
printf("%3.0f %6.1f\n", fahr, celsius);
fahr = fahr + step;
}
}
