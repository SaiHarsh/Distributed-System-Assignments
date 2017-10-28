#include  <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
void ChildProc(void)
{
    int i;
    for(i = 0; i < 100; i++)
    {
         printf("Child : %d from process <%d> : Parent <%d>\n",i, getpid(), getppid());
    }
}

void ParentProc(void)
{
    int i;
    for(i = 0; i < 20; i++)
    {
         printf("Parent : %d from process <%d> : Parent <%d>\n",i, getpid(), getppid());
    }
}

int main(void)
{
     pid_t child;
     child = fork();

     if(child == 0)
     {
          ChildProc();
     }
     else
     {
          ParentProc();
         // waitpid(child,NULL,0);
     }

}
