// program write in shared memory
// https://stackoverflow.com/questions/5656530/how-to-use-shared-memory-with-linux-in-c

#include <string.h>
#include <unistd.h>
#include <stdio.h>

#include "compartir.h"

int main() {
	char* parent_message = "hello";  // parent process will write this message
	char* child_message = "goodbye"; // child process will then write this one

	void* shmem = create_shared_memory(128);

	memcpy(shmem, parent_message, sizeof(parent_message));

	int pid = fork();

	if (pid == 0) {
		printf("Child read: %s\n", shmem);
		memcpy(shmem, child_message, sizeof(child_message));
		printf("Child wrote: %s\n", shmem);

	} else {
		printf("Parent read: %s\n", shmem);
		sleep(1);
		printf("After 1s, parent read: %s\n", shmem);
	}
}
