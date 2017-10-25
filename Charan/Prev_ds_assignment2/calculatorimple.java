package ds_assignment2;

import java.rmi.RemoteException; 
import java.rmi.server.UnicastRemoteObject; 

public class calculatorimple extends UnicastRemoteObject implements calci
{
	protected calculatorimple() throws RemoteException 
	{ 
		super(); 
	} 
	public long add(long a, long b) throws RemoteException 
	{ 
		return a+b; 

	} 
}
