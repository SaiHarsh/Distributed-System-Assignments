#include <map>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <algorithm>
#include <mpi.h>
#include <cmath>

using namespace std;


void masterProcessor(int processer_size,vector<string> inputFiles,int numbeFiles,string command);
void slaveProcessor(int processer_num);

int main(int argc, char const *argv[])
{
	int processer_size,processer_num;

	MPI_Init(NULL, NULL);
	MPI_Comm_size(MPI_COMM_WORLD, &processer_size);
	MPI_Comm_rank(MPI_COMM_WORLD, &processer_num);

	if(processer_num==0)
	{
		string str = "python q1_tokenize.py ";
		vector<string> inputFiles;
		for (int i = 1; i < argc; ++i)
		{
			str = str + argv[i] + " ";
			inputFiles.push_back(argv[i]);
		}
		masterProcessor(processer_size-1,inputFiles,argc - 1,str.c_str());
	}
	else
		slaveProcessor(processer_num);

	MPI_Finalize ();
	return 0;
}

void masterProcessor(int num_of_Slaves,vector<string> inputFiles,int numbeFiles,string command)
{
	MPI_Status status;
	int number = 0,input_size;
	string line;
	vector<string> list;
	
	system(command.c_str());

	ifstream file("output.txt");

	while (getline(file, line))
		list.push_back(line);

	std::sort(list.begin(), list.end());
	list.erase(std::unique(list.begin(), list.end()), list.end());

	input_size = list.size();
	int chunk_size = input_size / num_of_Slaves;
	
	for(int i=1;i < num_of_Slaves;i++,number += chunk_size)
	{
		MPI_Send(&chunk_size, 1, MPI_INT, i, i, MPI_COMM_WORLD);
		for(int j=number;j<(number+chunk_size);j++)
			MPI_Send(list[j].c_str(), list[j].size(), MPI_CHAR, i, i, MPI_COMM_WORLD);
		MPI_Send(&numbeFiles, 1, MPI_INT, i, i, MPI_COMM_WORLD);
	}
	chunk_size = input_size - number;

	MPI_Send(&chunk_size, 1, MPI_INT, num_of_Slaves, num_of_Slaves, MPI_COMM_WORLD);
	for(int j=number;j<input_size;j++)
		MPI_Send(list[j].c_str(), list[j].size(), MPI_CHAR, num_of_Slaves, num_of_Slaves, MPI_COMM_WORLD);
	MPI_Send(&numbeFiles, 1, MPI_INT, num_of_Slaves, num_of_Slaves, MPI_COMM_WORLD);

	sort(inputFiles.begin(), inputFiles.end());

	for (int i = 0,counter=0; i < inputFiles.size(); ++i,counter++)
	{
		string commandForFile = "python q1_tokenize.py " + inputFiles[i];
		system(commandForFile.c_str());
		printf("%s\n",inputFiles[i].c_str());
		MPI_Barrier(MPI_COMM_WORLD);
		
		int recv_size,count,max = 0;
		for (int i = 1; i <=num_of_Slaves; ++i)
		{
			MPI_Recv(&recv_size,1, MPI_INT, i,0, MPI_COMM_WORLD, &status);
			for (int j = 0; j < recv_size; ++j)
			{
				char buffer[5000] = { '\0' };
				MPI_Recv(buffer, 1000, MPI_CHAR, i, 0, MPI_COMM_WORLD, &status);
				MPI_Recv(&count, 1, MPI_INT, i, 0, MPI_COMM_WORLD, &status);
				if(max < count) max = count;
			}
		}
		MPI_Barrier(MPI_COMM_WORLD);

		for (int i = 1; i <=num_of_Slaves; ++i)
			MPI_Send(&max, 1, MPI_INT, i, i, MPI_COMM_WORLD);

		double val;
		for (int i = 1; i <=num_of_Slaves; ++i)
		{
			MPI_Recv(&recv_size,1, MPI_INT, i,0, MPI_COMM_WORLD, &status);
			for (int j = 0; j < recv_size; ++j)
			{
				char buffer[5000] = { '\0' };
				MPI_Recv(buffer, 1000, MPI_CHAR, i, 0, MPI_COMM_WORLD, &status);
				MPI_Recv(&val, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD, &status);
				printf("%s %0.2lf\n",buffer,val);
			}
		}
		
		if((counter)!=inputFiles.size())
			printf("\n");

		MPI_Barrier(MPI_COMM_WORLD);
	}
}

double calculateVal(double val)
{
	val=0.5 + (0.5)*(val);
	return floor(val * 100000000 + 0.5)/100000000;
}
void slaveProcessor(int processer_num)
{
	int run;
	MPI_Status status;
	int len;

	map<string, int> wordCount;
	std::vector<string> words;

	
	MPI_Recv(&len, 1, MPI_INT, 0, processer_num, MPI_COMM_WORLD, &status);
	for(int i=0;i<len;i++)
	{
		char buffer[5000] = { '\0' };		
		MPI_Recv(buffer, 1000, MPI_CHAR, 0, processer_num, MPI_COMM_WORLD, &status);
		wordCount[buffer] = 0;
		words.push_back(buffer);
	}
	MPI_Recv(&run, 1, MPI_INT, 0, processer_num, MPI_COMM_WORLD, &status);

	for (int i = 0; i < run; ++i)
	{
		int max, processer_size;

		MPI_Barrier(MPI_COMM_WORLD);
		for (int i = 0; i < words.size(); ++i)
			wordCount[words[i]] = 0;
		static const char* fileName = "output.txt";



		ifstream fileStream(fileName);
		if (fileStream.is_open())
			while (fileStream.good())
			{
				string word;
				fileStream >> word;
				if (wordCount.find(word) != wordCount.end())
					wordCount[word]++;
			}
		MPI_Comm_size(MPI_COMM_WORLD, &processer_size);



		int tempValReceived = 0;
		if(processer_num > 1)
			MPI_Recv(&tempValReceived, 1, MPI_INT, processer_num - 1, processer_num, MPI_COMM_WORLD, &status);
		tempValReceived = wordCount.size();





		MPI_Send(&tempValReceived,1,MPI_INT, 0, 0, MPI_COMM_WORLD);
		for (map<string, int>::const_iterator iter = wordCount.begin(); iter != wordCount.end(); iter++) 
		{
			string str(iter->first);
			int tempValReceived = int(iter->second);
			MPI_Send(str.c_str(), str.length(), MPI_CHAR, 0,0,MPI_COMM_WORLD);
			MPI_Send(&tempValReceived, 1, MPI_INT, 0,0,MPI_COMM_WORLD);
		}
		if((processer_size-1)!=processer_num)
			MPI_Send(&tempValReceived,1,MPI_INT, processer_num+1, processer_num+1, MPI_COMM_WORLD);



		MPI_Barrier(MPI_COMM_WORLD);



		MPI_Recv(&max, 1, MPI_DOUBLE, 0, processer_num, MPI_COMM_WORLD, &status);
		MPI_Comm_size(MPI_COMM_WORLD, &processer_size);
		if(processer_num > 1)
			MPI_Recv(&tempValReceived, 1, MPI_INT, processer_num - 1, processer_num, MPI_COMM_WORLD, &status);
		tempValReceived = wordCount.size();



		MPI_Send(&tempValReceived,1,MPI_INT, 0, 0, MPI_COMM_WORLD);
		for (map<string, int>::const_iterator iter = wordCount.begin(); iter != wordCount.end(); iter++) 
		{
			double val = calculateVal(double(iter->second)/double(max));
			MPI_Send(iter->first.c_str(), iter->first.length(), MPI_CHAR, 0,0,MPI_COMM_WORLD);
			MPI_Send(&val, 1, MPI_DOUBLE, 0,0,MPI_COMM_WORLD);
		}
		if((processer_size-1)!=processer_num)
			MPI_Send(&tempValReceived,1,MPI_INT, processer_num+1, processer_num+1, MPI_COMM_WORLD);



		MPI_Barrier(MPI_COMM_WORLD);
	}
}
