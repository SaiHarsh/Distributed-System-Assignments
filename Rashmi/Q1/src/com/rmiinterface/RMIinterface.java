package com.rmiinterface;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.Date;

import com.rmiserver.Transaction;

public interface RMIinterface extends Remote{
	public String deposit(int number, double amount) throws RemoteException;
	public String withdraw(int number, double amount) throws RemoteException;
	public String balance(int number) throws RemoteException;
	public java.util.List<Transaction> transaction(int number, Date fDate, Date toDate) throws RemoteException;
}