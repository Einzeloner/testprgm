#include <stdio.h>
 float main () {
	float far;
	for (far = 300; far >= 0; far = far - 20)
             printf("%3.1f %6.1f\n", far, (far - 32)*(5.0/9.0));
	}
