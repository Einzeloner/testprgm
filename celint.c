#include <stdio.h>
/* converting celsius to farenheit in this table */
int main (){
{
printf("Celsius to farenheit table\n");
}
int fahr, celsius;
int step, upper, lower;

/* define step, upper and lower here. */

/* step is the increment in my understanding */

/* upper is the upper limit of the temp scale */

/* and lower is the lower limit of the temp scale */

/* as for what do they do here's the explanation in my understanding based on f.c */

	lower = 0;
	step = 20;
	upper = 300;

celsius = lower;
while (celsius <= upper){
fahr = (9 * celsius/5) + 32;
printf( "%d\t %d\n", celsius, fahr);

/* from what I understand  this is going to print the required table with celsius on 
   the left and fahr on the right  like f.c  */
celsius = celsius + step;
}
}
 /* compile 1 - it did something different as it simply printed celsius and fahr until
 the while condition was true and not the values */

 /* changing the printf function, maybe that'll solve the problem */

/* compile 2 -  changed the printf function to {%d\t %d\n, celsius, fahr}
                and the error message was that %d is used for int not float */

/* changing the the condition in printf to %f */

/* compile 3 - ayyyyyyyyyyyyyy it worked! No errors, fuck yeah */




/* before compile 4 - changed the simple %f to %3.2f because it was a mess of decimals
                      before in the table */
/* yeah much better lol */


/* before compile 5- trying to do this in int instead of float as I don't want decimals */


/* it worked flawlessly, now going forward. will probably rename this to celint
 and make a new one for float named celfloat */
