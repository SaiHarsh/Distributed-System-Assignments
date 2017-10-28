#include <mpi.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "mergeSort.h"
 
using namespace std;

int output_array[1000],size = 0;

void masterProcessor(int num_of_slaves,int input_array[],int input_size);
void slaveProcessor();

void merge2Arrays(int arr1[], int output_array[],int n1,int n2);
void sendChunkToProcessor(int i,int number,int chunk, int input_array[]);

int main(int argc, char** argv) 
{
    int processer_rank, processer_size;
    
    MPI_Init(NULL, NULL);
    MPI_Comm_size(MPI_COMM_WORLD, &processer_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &processer_rank);
    processer_size = processer_size - 1;

    int input_size=atoi(argv[1]),input_array[1000];
    //scanf("%d", &input_size);
    for (int i = 0,j=2; i < input_size; i++,j++)
        input_array[i]=atoi(argv[j]);
        //scanf("%d", &input_array[i]);

    if (processer_rank == 0) 
        masterProcessor(processer_size,input_array,input_size);        
    else 
        slaveProcessor();
    MPI_Finalize();
    return 0;
}

void masterProcessor(int num_of_slaves,int input_array[],int input_size)
{
    MPI_Status status;
    
    int chunk = input_size / num_of_slaves;
    int number = 0;
    for(int i=1; i < num_of_slaves;i++,number = number + chunk)
        sendChunkToProcessor(i,number,chunk,input_array);
    
        int temp_index = 0,temp[input_size];
     
        for(int j=number;j<input_size;j++)
            temp[temp_index++] = input_array[j];
     
        MPI_Send(temp, temp_index, MPI_INT, num_of_slaves, 0, MPI_COMM_WORLD);   
        MPI_Barrier(MPI_COMM_WORLD); 

    
        int arrPartial[num_of_slaves+1][input_size];
        
        for(int i=0; i < num_of_slaves; i++)
        {
            int intArray[input_size], len, arrPartial_index = 0;

            MPI_Recv(intArray, input_size, MPI_INT, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
            MPI_Get_count(&status, MPI_INT, &len);
            
            arrPartial[i][arrPartial_index++] = len;
            len = len - 1;

            for(int j=0;j<=len;j++,arrPartial_index++)
                arrPartial[i][arrPartial_index] = intArray[j]; 
        }
        
        MPI_Barrier(MPI_COMM_WORLD);

        for(int i=1;i<=arrPartial[0][0];i++)
            output_array[i-1] = arrPartial[0][i];
        size += arrPartial[0][0];
        
        for(int i=1;i<num_of_slaves;i++)
            merge2Arrays(arrPartial[i], output_array,arrPartial[i][0], size-1);

        for (int i = 0; i <= (input_size-1); ++i)
            printf("%d ", output_array[i]);
        printf("\n");
}

void slaveProcessor()
{        
    MPI_Status status;
    int len;
    int arrPartial[100];

    MPI_Recv(arrPartial, 100, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
    MPI_Get_count(&status, MPI_INT, &len);
    MPI_Barrier(MPI_COMM_WORLD);

    mergeSort(arrPartial, 0, len - 1);

    MPI_Send(arrPartial, len, MPI_INT, 0, 0, MPI_COMM_WORLD);
    MPI_Barrier(MPI_COMM_WORLD);
    
}

void merge2Arrays(int arr1[], int output_array[],int n1,int n2)
{
    int temp_array[50];    
    int i=0, j=1, k=0;
    
    while(i<=n2 && j<=n1) 
        if(output_array[i]<arr1[j])
            temp_array[k++]=output_array[i++];
        else
            temp_array[k++]=arr1[j++];

    while(j<=n1)    
        temp_array[k++]=arr1[j++];

    while(i<=n2) 
        temp_array[k++]=output_array[i++];
        
    
    for(i=0;i<=k;i++)
        output_array[i]=temp_array[i];
    
    size = k+1;
}

void sendChunkToProcessor(int i,int number,int chunk,int input_array[])
{
    int temp[chunk+1], temp_index=0;
    for(int j=number;j<(number+chunk);j++)
        temp[temp_index++] = input_array[j];
    MPI_Send(temp, chunk, MPI_INT, i, 0, MPI_COMM_WORLD);
}