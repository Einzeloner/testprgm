/* To verify that the EOF value is either 0 or 1 */


#include <stdio.h>
int main()
{
	int c;
	c = getchar();
	while (c = EOF)
		putchar(EOF);
}
/* If this prints no char then the value of EOF is 0 */
