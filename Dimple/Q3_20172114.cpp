    #include <stdio.h>  
    #include <stdlib.h>  
    #include <malloc.h>  
    #include <math.h>  
    #include <mpi.h>  
    #define A(i,j) A[i*N+j]  
    #define MST(i,j) MST[i*n*p+j]  
    #define MAX 1000  
    int N;  
    int n;  
    int p;  
    int i,j,k;  
      
    double l;  
      
    int *D,*C,*W,*J;  
      
    int *A;  
    int *MST;  
    int myid;  
    MPI_Status status;  
      
    int readInput()  
    {  
        int i,j;  
        int p1;  
        p1=p;  
        int E;
        scanf("%d %d",&N,&E);
        n=N/p1;  
        if(N%p1!=0) n++;  
        A=(int*)malloc(sizeof(int)*(n*p1)*N);  
        if(A==NULL)
        {  
            printf("Error when allocating memory\n");  
            exit(0);  
        } 
        for(i=0;i<N;i++)  
        for(j=0;j<N;j++)  
            A(i,j)=0;
        int u,v,weight;
        while(E--)
        {
            scanf("%d %d %d",&u,&v,&weight);
            A(u,v)=weight;
            A(v,u)=weight;
        }

        for(i=N;i<n*p1;i++)  
        for(j=0;j<N;j++)  
            A(i,j)=MAX-1;  
        p=p1;  
        return(0);  
      
    }  
      
       
      
    int min(int a,int b)  
    {  
      return(a<b?a:b);  
    }  
      
    int connected()  
    {  
        int i;  
        int flag;  
        flag=1;  
        for(i=1;i<N;i++)  
            if(D[i]!=D[0])  
            {  
                flag=0;  
                break;  
            }  
            return(flag);  
    }  
      
    void D_to_C()  
    {  
        int i,j;  
        for(i=0;i<n;i++){  
        W[n*myid+i]=MAX;  
        for(j=N-1;j>=0;j--)  
            if((A(i,j)>0)&&(D[j]!=D[n*myid+i])&&(A(i,j)<=W[n*myid+i]))  
            {  
                C[n*myid+i]=D[j];  
                W[n*myid+i]=A(i,j);  
                J[n*myid+i]=j;  
            }  
        if(W[n*myid+i]==MAX) C[n*myid+i]=D[n*myid+i];  
      }  
      
    }  
      
      
    void C_to_C()  
    {  
        int tempw,tempj;  
        for(i=0;i<n;i++){  
            tempj=N+1;  
            tempw=MAX;  
            for(j=N-1;j>=0;j--)  
                if((D[j]==n*myid+i)&&(C[j]!=n*myid+i)&&(W[j]<=tempw))  
                {  
                    C[myid*n+i]=C[j];  
                    tempw=W[j];  
                    tempj=j;  
                }  
            if(myid==0)  
            {  
                if((tempj<N)&&(J[tempj]<N))   
                MST(tempj,J[tempj])=MST(J[tempj],tempj)=tempw;  
                for(j=1;j<p;j++)  
                {  
                    MPI_Recv(&tempj,1,MPI_INT,j,j,MPI_COMM_WORLD,&status);  
                    MPI_Recv(&tempw,1,MPI_INT,j,0,MPI_COMM_WORLD,&status);  
                    if((tempj<N)&&(tempw <N))MST(tempj,tempw)=MST(tempw,tempj)=A(tempj,tempw);  
                }  
            }  
            else  
            {  
                MPI_Send(&tempj,1,MPI_INT,0,myid,MPI_COMM_WORLD);  
                MPI_Send(&J[tempj],1,MPI_INT,0,0,MPI_COMM_WORLD);  
            }  
            MPI_Barrier(MPI_COMM_WORLD);  
        }  
      
    }  
      
      
    void CC_to_C()  
    {  
        for(i=0;i<n;i++)  
            C[myid*n+i]=C[C[myid*n+i]];  
      
    }  
      
      
    void CD_to_D()  
    {  
        for(i=0;i<n;i++)  
            D[myid*n+i]=min(C[myid*n+i],D[C[myid*n+i]]);  
      
    }  
      
      
      
    int main(int argc,char **argv)  
    {  
        int i,j,k;  
        int group_size;  
      
        MPI_Init(&argc,&argv);  
        MPI_Comm_size(MPI_COMM_WORLD,&group_size);  
        MPI_Comm_rank(MPI_COMM_WORLD,&myid);  
      
        p=group_size;  
        if(myid==0)  
        {  
            readInput();  
            MST=(int*)malloc(sizeof(int)*n*p*n*p);  
        }  
      
        MPI_Bcast(&N,1,MPI_INT,0,MPI_COMM_WORLD);  
        if(myid!=0)
        {  
            n=N/p;  
            if(N%p!=0) n++;  
        }  
      
        D=(int*)malloc(sizeof(int)*(n*p));  
        C=(int*)malloc(sizeof(int)*(n*p));  
        W=(int*)malloc(sizeof(int)*(n*p));  
        J=(int*)malloc(sizeof(int)*(n*p));  
      
        if(myid!=0)  
            A=(int*)malloc(sizeof(int)*n*N);  
      
        for(i=0;i<n;i++) 
            D[myid*n+i]=myid*n+i;  
        
        MPI_Gather(&D[myid*n],n,MPI_INT,D,n,MPI_INT,0,MPI_COMM_WORLD);  
        MPI_Bcast(D,N,MPI_INT,0,MPI_COMM_WORLD); 
        
        if(myid==0)  
            for(i=1;i<p;i++)  
                MPI_Send(&A(i*n,0),n*N,MPI_INT,i,i,MPI_COMM_WORLD);  
        else  
            MPI_Recv(A,n*N,MPI_INT,0,myid,MPI_COMM_WORLD,&status);  
        

        MPI_Barrier(MPI_COMM_WORLD);  
      
        l=log(N)/log(2);  
        i=1;  
        
        while(!connected())
        {  
           
            D_to_C();  
            MPI_Barrier(MPI_COMM_WORLD);  
            MPI_Gather(&C[n*myid],n,MPI_INT,C,n,MPI_INT,0,MPI_COMM_WORLD);  
            MPI_Gather(&W[n*myid],n,MPI_INT,W,n,MPI_INT,0,MPI_COMM_WORLD);  
            MPI_Bcast(C,N,MPI_INT,0,MPI_COMM_WORLD);   
            MPI_Bcast(W,N,MPI_INT,0,MPI_COMM_WORLD);   
            MPI_Barrier(MPI_COMM_WORLD);  
      
            C_to_C();  
            MPI_Barrier(MPI_COMM_WORLD);  
      
            MPI_Gather(&C[n*myid],n,MPI_INT,C,n,MPI_INT,0,MPI_COMM_WORLD);  
            MPI_Gather(&C[n*myid],n,MPI_INT,D,n,MPI_INT,0,MPI_COMM_WORLD);  
            MPI_Barrier(MPI_COMM_WORLD);  
      
            if(myid==0)  
                for(j=0;j<n;j++) D[j]=C[j];  
      
            for(k=0;k<l;k++)
            {  
                MPI_Bcast(C,N,MPI_INT,0,MPI_COMM_WORLD);   
                CC_to_C();  
                MPI_Gather(&C[n*myid],n,MPI_INT,C,n,MPI_INT,0,MPI_COMM_WORLD);  
            }  
            MPI_Bcast(C,N,MPI_INT,0,MPI_COMM_WORLD);   
            MPI_Bcast(D,N,MPI_INT,0,MPI_COMM_WORLD);   
      
            CD_to_D();  
            MPI_Gather(&D[n*myid],n,MPI_INT,D,n,MPI_INT,0,MPI_COMM_WORLD);  
            MPI_Bcast(D,N,MPI_INT,0,MPI_COMM_WORLD);   
        
            i++;  
        }  
        
        if(myid==0)
        {
            int sum=0;  
            for(i=0;i<N;i++)  
            {  
                for(j=0;j<N;j++)
                { 
                    sum+=  MST[i*n*p+j];  
                }
            }  
            printf("%d\n",sum/2);  
        }  
        
        MPI_Finalize();  
        return(0);  
    }  