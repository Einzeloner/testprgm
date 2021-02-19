#include <stdio.h>
/* characters count second version */
double main() {
	double nc;
	for (nc = 0; getchar() !=EOF; ++nc)
		;
	printf("%0.f\n", nc);
}
/* One thing about while and for loops is that they test at the top
 of the body of the loop before the body, which means it skips the body if there is nothing to be done */
