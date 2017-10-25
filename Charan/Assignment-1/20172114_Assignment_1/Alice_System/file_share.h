#include "status_bar.h"
int SocketNum;
void *RecievingThread(void *dummyPtr);
void *SendingThread(void *dummyPtr);
void file_share(int n)
{
	SocketNum=n;
    
    pthread_t thread1,thread2;
	pthread_create( &thread1, NULL, RecievingThread, NULL );
	pthread_create( &thread2, NULL, SendingThread, NULL );
	pthread_join( thread1, NULL);   
	pthread_join( thread2, NULL);
	
	close(SocketNum);
}



void UDP_FileSending(char FILENAME[])
{
	printf("Nothing\n");
}
void UDP_FileReceiving(char FILENAME[])
{
	printf("Nothing\n");

}

void TCP_FileSending(char FILENAME[])
{
	printf("%s\n",FILENAME );
	int fd;
	int bytes_sent = 0;
	char file_size[BUFSIZ];
	struct stat FILE_STAT;
	fd = open(FILENAME, O_RDONLY);
	if (fd == -1)
		fprintf(stderr, "%s", strerror(errno));
	
	if (fstat(fd, &FILE_STAT) < 0)
		fprintf(stderr, "%s", strerror(errno));

	sprintf(file_size, "%ld", FILE_STAT.st_size);

	int len = send(SocketNum, file_size, sizeof(file_size), 0);
	if (len < 0)		
		fprintf(stderr, "%s", strerror(errno));

	int offset = 0;
	int remaining_data = FILE_STAT.st_size;

	while (((bytes_sent = sendfile(SocketNum, fd, 0, BUFSIZ)) > 0) && (remaining_data >= 0))
	{
		remaining_data -= bytes_sent;
		status_bar(1,FILENAME,(FILE_STAT.st_size - remaining_data), (FILE_STAT.st_size));
	}
	close(fd);

	printf("\nSent file\n");
}

void TCP_FileReceiving(char FILENAME[])
{
	ssize_t len;
	char buffer_client[BUFSIZ];
	int file_size;
	FILE *received_file;
	int remaining_data = 0;

	recv(SocketNum, buffer_client, BUFSIZ, 0);
	file_size = atoi(buffer_client);
	
	received_file = fopen(FILENAME, "w");
	if (received_file == NULL)
		fprintf(stderr, "%s\n", strerror(errno));

	remaining_data = file_size;
	while (((remaining_data > 0) && ((len = recv(SocketNum, buffer_client, BUFSIZ, 0)) > 0)) )
	{
		fwrite(buffer_client, sizeof(char), len, received_file);
		remaining_data -= len;
		status_bar(0,FILENAME,file_size - remaining_data, file_size);
	}
	
	fclose(received_file);
	printf("\nReceived file\n");
}


void *RecievingThread(void *dummyPtr)
{	
	while(1)
	{
		int bytes_received;
		char received_data[1024];
		if(bytes_received=recv(SocketNum,received_data,1024,0))
		{
			received_data[bytes_received]='\0';
			printf("Bob: %s",received_data );
			
			char *token;
			token = strtok(received_data, " ");

			if (!strcmp(token,"Sending"))
			{			   
				char FilePath[100],*FileName,*ConnectionMode;
				
				strcpy(FilePath,"Alice_System/");
				FileName=strtok(NULL, " ");
				
				int slen=strlen(FilePath);
				for (int i = 0; i < strlen(FileName); i++)
						FilePath[slen++]=FileName[i];
				FilePath[slen]='\0';
				
				ConnectionMode = strtok(NULL, " ");
				
				if (!strcmp(ConnectionMode,"TCP\n"))
					TCP_FileReceiving(FilePath);
				else if (!strcmp(ConnectionMode,"UDP\n"))
					UDP_FileReceiving(FilePath);
				else
					return 0;
			}
		}
	}

}

void *SendingThread(void *dummyPtr)
{
	while(1)
	{
		char buffer[1024],got_data[1024];
		fgets(buffer,1023,stdin);
		strcpy(got_data,buffer);
		send(SocketNum, got_data,strlen(got_data), 0); 
			   
			char *token;
			token = strtok(got_data, " ");

			if (!strcmp(token,"Sending"))
			{			   
				char FilePath[100],*FileName,*ConnectionMode;
				
				strcpy(FilePath,"Alice_System/");
				FileName=strtok(NULL, " ");
				
				int slen=strlen(FilePath);
				for (int i = 0; i < strlen(FileName); i++)
						FilePath[slen++]=FileName[i];
				
				FilePath[slen]='\0';
				
				ConnectionMode = strtok(NULL, " ");
				
				if (!strcmp(ConnectionMode,"TCP\n"))
					TCP_FileSending(FilePath);
				else if (!strcmp(ConnectionMode,"UDP\n"))
					UDP_FileSending(FilePath);
				else
					return 0;
			}	
	}
}

