#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

void inicialitza_pipe (int *fd)
{
	if ((pipe(fd)) == -1)
	{
		printf ("No hem pogut fer el pipe.");
		exit (EXIT_FAILURE);
	}
}

//stdin		Entrada estàndard 0
//stdout	Sortida estàndard 1
// pipe(3p)
int main ()
{
	int fdin[2], fdout[2];

	// Copy paste `man 3p pipe`
	const int BSIZE = 100;
	char buf[BSIZE];
	ssize_t nbytes;

	inicialitza_pipe (fdin);
	inicialitza_pipe (fdout);

	// Comprovar errors
	switch (fork ())
	{
	case -1: /* Error */
		printf ("Error, no ha pogut fer el fork.\n");
		return EXIT_FAILURE;

	case 0: /* Fill */
		close (fdout[1]);			/* Escriure final no és usat. */
		close (fdin[0]);
		dup2 (fdout[0], STDIN_FILENO);
		dup2 (fdin[1], STDOUT_FILENO);
		printf ("Estic viu! Sóc el fill\n");
		execl ("./parla.py", NULL);//"./parla.py", NULL);
		break;
	default: /* Pare */
		close (fdout[0]);			/* Llegir final no és usat. */
		close (fdin[1]);
		printf ("Sóc  el pare.\n");
		write (fdout[1], "Hello world\n", 12);
		wait(NULL); // Esperem el fill.
		nbytes = read(fdin[0], buf, BSIZE);   /* Get data from pipe */
		printf ("Del fill llegit: %s", buf);
		printf ("Nombre de caràcters?: %d, %d\n", nbytes, strlen(buf));
		printf ("Ja he matat el fill.\n");
	}

	return EXIT_SUCCESS;
}
