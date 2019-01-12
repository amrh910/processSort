//Amr Hammam - 23180137 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/file.h>

int main()
{
	//similar to assignment 1
	int pid = fork();
	int fd = pid;
	//fork check
	if (pid < 0)
	{
		printf("Fork status: FAILED.\n");
	}
	else if (pid == 0)
	{
		sleep(1); //just to be safe
		//lock check
		if(lockf(fd, F_LOCK, 5) == -1)
		{
			printf( "error: LOCKED\n");
			exit(1);
		}
		printf("Executing... \n");
		execlp("python3", "python3", "./fileWr.py", NULL);
		printf("error executing fileWr.py\n");
		//unlock
		if(lockf(fd, F_ULOCK, 5) == -1)
		{
			printf("resolved: UNLOCKED\n");
			exit(1);
		}
		exit(EXIT_FAILURE);		
	}
	else 
	{
		wait(NULL);
		return EXIT_SUCCESS;
	}
	return 0;
}