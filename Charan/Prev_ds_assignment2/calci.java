package ds_assignment2;

import java.rmi.Remote; 
import java.rmi.RemoteException; 
public interface calci extends Remote 
{ 
	public long add(long a, long b) throws RemoteException; 
} 

