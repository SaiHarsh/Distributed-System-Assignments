#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <mpi.h>
#include <cstdlib>
#include <algorithm>

#define MAX_LENGTH 50000

using namespace std;

void masterProcessor(int num_of_slaves,string fileName, string token);
void slaveProcessor(int processer_num,string token);

void sendchunkToProcessor(int i,int number,int chunk_size,vector<string> list);
char* stradd(const char* a, const char* b);
void search(vector<string> &list, string token,int processer_num);

int main(int argc, char *argv[])
{

    int processer_size, processer_rank;

	MPI_Init ( &argc, &argv );
    MPI_Comm_size(MPI_COMM_WORLD, &processer_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &processer_rank);
    processer_size = processer_size - 1 ;

	if(processer_rank == 0)
		masterProcessor(processer_size,argv[argc-2],argv[argc-1]);
	else
		slaveProcessor(processer_rank,argv[argc-1]);
	MPI_Finalize ();
    return 0;
}
void masterProcessor(int num_of_slaves,string fileName, string token)
{
	MPI_Status status;
		vector<string> list;
		ifstream file(fileName.c_str());
	    string str; 
	    int number = 0,input_size;
	    while (getline(file, str))
	    {
	        list.push_back(str);
	    }
	    input_size = list.size();
	    int chunk_size = input_size /num_of_slaves;

	    for(int i=1; i < num_of_slaves;i++,number = number + chunk_size)
	        sendchunkToProcessor(i,number,chunk_size,list);

        chunk_size = input_size - number;
        
        MPI_Send(&chunk_size, 1, MPI_INT, num_of_slaves, num_of_slaves, MPI_COMM_WORLD);
        for(int i=number;i<input_size;i++)
            MPI_Send(list[i].c_str(), list[i].size(), MPI_CHAR, num_of_slaves, num_of_slaves, MPI_COMM_WORLD);
 
        MPI_Barrier(MPI_COMM_WORLD);
        int recv_size, total = 0;
        for (int i = 1; i <=num_of_slaves; i++)
        {
        	MPI_Recv(&recv_size,1, MPI_INT, i,0, MPI_COMM_WORLD, &status);
        	for (int j = 0; j < recv_size; j++)
        	{
        		char buffer[MAX_LENGTH] = { '\0' };
        		MPI_Recv(buffer, MAX_LENGTH, MPI_CHAR, i, 0, MPI_COMM_WORLD, &status);
        		total += 1;
        		for (int i = 0; i < strlen(buffer); i++)
        			printf("%c",buffer[i]);
        		printf("\n");
        	}
        }
        printf("total=%d\n",total ); 
}

void sendchunkToProcessor(int i,int number,int chunk_size,vector<string> list)
{
	MPI_Send(&chunk_size, 1, MPI_INT, i, i, MPI_COMM_WORLD);
    for(int j=number;j<(number+chunk_size);j++)
        MPI_Send(list[j].c_str(), list[j].size(), MPI_CHAR, i, i, MPI_COMM_WORLD);
}

void slaveProcessor(int processer_num,string token)
{
		MPI_Status status;
		int len;
        vector<string> partial_list;
        
        MPI_Recv(&len, 1, MPI_INT, 0, processer_num, MPI_COMM_WORLD, &status);
        for(int i=0;i<len;i++)
        {
        	char buffer[MAX_LENGTH] = { '\0' };
        	MPI_Recv(buffer, MAX_LENGTH, MPI_CHAR, 0, processer_num, MPI_COMM_WORLD, &status);
        	partial_list.push_back(stradd(buffer, "\0"));
        }
        MPI_Get_count(&status, MPI_INT, &len);
        MPI_Barrier(MPI_COMM_WORLD);    
        search(partial_list, token, processer_num);
}

char* stradd(const char* a, const char* b)
{
    size_t len = strlen(a) + strlen(b);
    char *ret = (char*)malloc(len * sizeof(char) + 1);
    *ret = '\0';
    return strcat(strcat(ret, a) ,b);
}

void search(vector<string> &list, string token,int processer_num)
{
        int temp=1;
	    int processer_size;
	    MPI_Comm_size(MPI_COMM_WORLD, &processer_size);

	    vector<string> send;		
		MPI_Status status;

		for(int i=0;i<list.size();i++)
	    	if (list[i].find(token) != std::string::npos) 
	    		send.push_back(stradd(list[i].c_str(), "\0"));

		if(processer_num > 1)
			MPI_Recv(&temp, 1, MPI_INT, processer_num - 1, processer_num, MPI_COMM_WORLD, &status);

	    temp = send.size();

	    MPI_Send(&temp,1,MPI_INT, 0, 0, MPI_COMM_WORLD);
	    
	    for (int i = 0; i < temp; i++)
	    	MPI_Send(send[i].c_str(), send[i].size(), MPI_CHAR, 0, 0, MPI_COMM_WORLD);
	    
	    if((processer_size-1)!=processer_num)
	    	MPI_Send(&temp,1,MPI_INT, processer_num+1, processer_num+1, MPI_COMM_WORLD);

}