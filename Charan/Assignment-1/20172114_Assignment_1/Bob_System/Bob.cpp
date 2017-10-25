#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>
#include <pthread.h>


#include <sys/mman.h>
#include <sys/wait.h>
#include <fcntl.h>

#include <sys/sendfile.h>
#include <arpa/inet.h>
#include <sys/stat.h>

#include "file_share.h"

int connectionSocket;

void TCP_server(int bind_port_number);
void TCP_client(int server_port_number);
int main(int argc, char const *argv[])
{

	printf("Bob is activated\n");
	int serverORclient=atoi(argv[1]);
	if(serverORclient)TCP_client(atoi(argv[2]));
	else TCP_server(atoi(argv[2]));

	return 0;
}

void TCP_server(int bind_port_number)
{
	int sock;
	struct sockaddr_in server_addr,client_addr; 

	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) 
	{
		perror("Socket");
		exit(1);
	}

	server_addr.sin_family = AF_INET;         
	server_addr.sin_port = htons(bind_port_number);     
	server_addr.sin_addr.s_addr = INADDR_ANY; 
	bzero(&(server_addr.sin_zero),8); 


	if (bind(sock, (struct sockaddr *)&server_addr, sizeof(struct sockaddr))== -1) 
	{
		perror("Unable to bind");
		exit(1);
	}

	// Listening to connections
	if (listen(sock, 5) == -1) //maximum connections listening to 5
	{
		perror("Listen");
		exit(1);
	}
	fflush(stdout);
	// Accepting connections
	while((connectionSocket=accept(sock , (struct sockaddr*)NULL,NULL))<0);

	printf("[CONNECTED]\n");

	file_share(connectionSocket);
}
void TCP_client(int server_port_number)
{
	struct sockaddr_in serv_addr;

	connectionSocket = socket(AF_INET,SOCK_STREAM,0);
	if(connectionSocket<0)
	{
		printf("ERROR WHILE CREATING A SOCKET\n");
		return;
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(server_port_number);
	serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	bzero(&(serv_addr.sin_zero),8);

	while (connect(connectionSocket, (struct sockaddr *)&serv_addr,sizeof(struct sockaddr)) < 0);

	printf("[CONNECTED]\n");


	file_share(connectionSocket);	

}