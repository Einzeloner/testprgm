#include <stdio.h>
/* characters count second version */
double main() {
	double nc;
	for (nc = 0; getchar() !=EOF; ++nc);
	printf("%0.f\n", nc);
}
