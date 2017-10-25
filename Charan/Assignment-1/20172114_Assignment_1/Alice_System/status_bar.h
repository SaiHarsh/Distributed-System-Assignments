int status_bar(int sendingORreceiving,char *FILENAME,int transmission_status,int file_size)
{
	int j;
		printf("\r");
		int progress = (25*transmission_status)/file_size;
		if (sendingORreceiving)
			printf("Sending %s [",FILENAME);
		else
			printf("Receiving %s [",FILENAME);
		for(j=0;j<=progress;j++)
		{
			printf("█");
		}
		for(j=0;j<25-progress;j++)
		{
			printf("  ");
		}
		printf("] %d%%",progress*4);

		fflush(stdout);
}
