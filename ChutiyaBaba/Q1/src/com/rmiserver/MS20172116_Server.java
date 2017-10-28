package com.rmiserver;

import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.Date;
import java.util.Hashtable;
import java.util.List;

import com.rmiinterface.MS20172116_Interface;

public class MS20172116_Server extends UnicastRemoteObject implements MS20172116_Interface{
	private static final long serialVersionUID = 1L;
	protected MS20172116_Server() throws RemoteException {
		super();
	}
	private static List<Account> accounts = new ArrayList<Account>();
    static Hashtable<Integer, Integer> Table = new Hashtable<Integer, Integer>(); // Creating Hash Table
	
	@Override
	   public String deposit(int Account_Number, double amount) throws RemoteException{
		/*    double Current_Balance = 1000 + amount;
		      System.err.println("[Server: ] Successfully Add money " + Current_Balance + "of Account Number: "+ Account_Number);
		      return "[Server: ] Successfully Add money " + Current_Balance + "of Account Number: "+ Account_Number;*/
		      Integer i = Table.get(Account_Number);
		      if(i==null){
		         return "Account not found!";
		      }
		      else{
		            Account account = accounts.get(i);
		            System.err.println("The Index: " + i);
		            double amount1 = account.getBalance() + amount;
		            account.setBalance(amount1); 
		            account.addTransaction("Deposit", amount);
		            return "Successfully Added: "+ amount + " to A/C "+ Account_Number+ " Current Balance: " + account.getBalance() + "\n----------------------------------------";

		      }
		   }
		   
		   @Override
		   public String withdraw(int Account_Number, double amount) throws RemoteException{
		/*    double Current_Balance = 1000 - amount;
		      System.err.println("[Server: ] Success!!! Current Balance: " + Current_Balance + "of Account Number: "+ Account_Number);
		      return "[Server: ] Success!!! Current Balance: " + Current_Balance + "of Account Number: "+ Account_Number;*/
		      Integer i = Table.get(Account_Number);
		      if(i==null){
		         return "Account not found!";
		      }
		      else{
		    	  	Account account = accounts.get(i);
		            double amount1 = account.getBalance() - amount;
		    	  	account.setBalance(amount1); 
		            account.addTransaction("Withdraw", amount);
		            return "Successfully Deducted: "+ amount + " from A/C "+ Account_Number+ "\n Current Balance:" + account.getBalance() + "\n----------------------------------------";
		      }
		   }
		   
		   @Override
		   public String balance(int Account_Number) throws RemoteException{
			   Integer i = Table.get(Account_Number);
			   return "Your A/C: "+ Account_Number +" Balance: " + accounts.get(i).getBalance() + "\n----------------------------------------";
		   }
		   
		   @Override
		   public List<Transaction> transaction(int Account_Number, Date fromDate, Date toDate) throws RemoteException {		
				List<Transaction> statementList = new ArrayList<Transaction>();
				Integer i = Table.get(Account_Number);
			    if(i==null){
			         return statementList;
			      }
			    else{
					Account element = accounts.get(i);
					return element.getTransactionsByDate(fromDate, toDate);
				}
			}
			
			public static void main(String[] args){
				try {
					LocateRegistry.createRegistry(2020);
					Naming.rebind("//localhost:2020/Server", new MS20172116_Server());            
		            
		            Account account1 = new Account(100, "Sai Harsh", 10000, "8888");
		            accounts.add(account1);
		            Table.put(100,0);
		            
		    		account1 = new Account(101, "Sai Charan", 5000, "8888");
		    		accounts.add(account1);
		    		Table.put(101,1);
		            
		    		System.out.println("[Server Ready]");
		    		
		    		
		        } catch (Exception e) {
		        	System.err.println("Server exception: " + e.toString());
		          e.printStackTrace();
		        }
			}
}