#include <ctype.h>
#include <stdio.h>

// No funciona per CTRL-D
void treure_vasura (void) { while (getchar () != '\n'); }

int lectura_digit (void)
{
	char c;
	int r = 0;
	while (isdigit ((c = getchar ())))
		r = c - '0' + 10 * r;
	return r;
}
/*
 * Suposem que ningú fa anar el CTRL-D per entrar dades
 * Ja que o no llegeix res, o retorna un -1
 *
 */
int main ()
{
	char c;
	int i;

	printf ("No facis <instrucció>CTRL-D ;)\n");
	printf ("Fes <instrucció><enter>\n");
	printf ("Per acabar, esperi el mode input [»], llavors fes CTRL-D\n");
	printf ("\n» ");
	while ((c = getchar()) != EOF)
	{
		switch (c)
		{
		case 'd':
			switch (getchar())
			{
			case '\n':
				printf ("Vol eliminar tots els punts de parada (brakpoints)? (`s' o `n') ");
				while ((c = getchar ()) != EOF)
					if ( c == 'n' )
					{
						printf ("interpretat n");
						break;
					}
					else if ( c == 's' )
					{
						printf ("interpretat s");
						break;
					}
					else if ( c == '\n' )
					{
						printf ("Si us plau respon `s' o `n'.\n");
						printf ("Vol eliminar tots els punts de parada (brakpoints)? (`s' o `n') ");
					}
					else
					{
						printf ("Si us plau respon `s' o `n'.\n");
						printf ("Vol eliminar tots els punts de parada (brakpoints)? (`s' o `n') ");
						treure_vasura ();
					}
				treure_vasura ();
				break;
			case ' ':
				i = lectura_digit ();
				printf ("Llegit: %d", i);
				break;
			}
			break;
		case 'i':
		default:
		printf ("Instrucció erronia: `%c'\n", c);
		printf ("premi `h' per tenir ajuda\n");
		treure_vasura ();
		}
	printf ("\n» ");
	}
	printf ("\n");
return 0;
}
