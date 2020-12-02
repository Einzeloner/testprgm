#include <stdio.h>
/* Count charracters in input. First version. */
long main() {
	long nc;
	nc = 0;
	while(getchar() !=EOF)
		++nc;
	printf("%1d\n", nc);
}
