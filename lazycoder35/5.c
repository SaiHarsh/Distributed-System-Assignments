#include  <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
	int frk;
	frk = fork();
	if(frk ==0) {
		int frk1;
		frk1 = fork();
		if(frk1 == 0) {
			printf("P1 id: %d, pid: %d\n", getpid(), getppid());
		}

		else if(frk1>0) {
			printf("p2 id: %d, pid: %d\n",getpid(), getppid());
		}
	}

	else if(frk >0) {
		int frk2;
		frk2 = fork();
		if(frk2 == 0) {
			printf("p3 id: %d, pid: %d\n", getpid(), getppid());
		}
		else if(frk2 >0) {
			printf("p4 id: %d, pid: %d\n", getpid(), getppid());
		}
	}
}
