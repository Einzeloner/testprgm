#include <stdio.h>
float main(){
{
printf("The same celsius scale but in float\n");
}

float  celsius, fahr;
float  step, upper, lower;

	step = 20;
	upper = 300;
 	lower = 0;

celsius = lower;
while(celsius <= upper){
fahr = (9.0/5.0 * celsius) + 32.0;
printf("%3.1f %3.1f\n", celsius, fahr);
celsius = celsius + step;
}
}
