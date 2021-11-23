#include "main.h"
#include <stdio.h>
/**
 * print_to_98 - prints all natural numbers from n to 98,
 * followed by a new line.
 *
 * @n: number to start printing from.
 *
 * Return: Always 0.
 *
 */
void print_to_98(int n)
{
	int i, j;

	int sep1 = 0;
	int sep2 = 0;

	for (i = n; i < 99; i++)
	{
		printf("%d", i);

		if (i < 98)
		{
			putchar(44);
			putchar(32);
		}
	}

	for (j = n; j > 97; j--)
	{
		if (n > 98)
		{

			putchar(sep1);
			putchar(sep2);

			printf("%d", j);

			sep1 = 44;
			sep2 = 32;
		}
	}
	putchar(10);
}
