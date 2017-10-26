package com.rmiclient;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;  

import com.rmiinterface.RMIinterface;
import com.rmiserver.Transaction;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;


public class ClientOperation {

	private static RMIinterface look_up;

	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
		
		look_up = (RMIinterface) Naming.lookup("//localhost:2020/Server");			
		Scanner sc=new Scanner(System.in);  
		int Account_Number;
		String response;
        double Amount;
		while(1 > 0){
            System.out.println("Enter your choice"); 
            System.out.println("------------------------------\n D: Deposit\n W: Withdraw\n B:Balance\n T:Transaction Details\n------------------------------");       
            char choose = sc.next().charAt(0);
            switch(choose) {
               case 'D' :
                  System.out.println("You have choosen for Deposit!"); 
	       		  System.out.println("Enter your A/C Number:");  
	    		  Account_Number=sc.nextInt();
		   		  System.out.println("Enter Amount you want to Deposit");
		   		  Amount=sc.nextDouble();                  
		   		  response = look_up.deposit(Account_Number,Amount);
		   		  System.out.println("[Server:] "+ response);
		   		  break;
               case 'W' :
                  System.out.println("You have choosen for Withdraw!"); 
	       		  System.out.println("Enter your A/C Number:");  
	       		  Account_Number=sc.nextInt();
		   		  System.out.println("Enter Amount you want to Withdraw");  
		   		  Amount=sc.nextDouble();                  
		   		  response = look_up.withdraw(Account_Number,Amount);
		   		  System.out.println("[Server:] "+ response);
                  break;
               case 'B' :
                  System.out.println("You have choosen to Balance!"); 
                  System.out.println("Enter your A/C Number:");  
                  Account_Number=sc.nextInt();
		   		  response = look_up.balance(Account_Number);
		   		  System.out.println("[Server:] "+ response);                  
		   		  break;
               case 'T' :
                  System.out.println("You have choosen to Transaction Details!");
                  System.out.println("Enter your A/C Number:");  
                  Account_Number=sc.nextInt();
                  System.out.println("Enter From Date in dd/mm/yyyy format:");
                  SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy", Locale.ENGLISH);
                  Date fDate = null, toDate = null;
                  try {
  	                //Parsing the String
  	                fDate = dateFormat.parse(sc.next());
	  	            } catch (ParseException e) {
	  	            	e.printStackTrace();
	  	            	// TODO Auto-generated catch block
	  	            }
                  System.out.println("Enter to Date in dd/mm/yyyy format:");
                  try {
    	                //Parsing the String
    	                toDate = dateFormat.parse(sc.next());
  	  	            } catch (ParseException e) {
  	  	            	e.printStackTrace();
  	  	            	// TODO Auto-generated catch block
  	  	            }
                  List<Transaction> statementList = look_up.transaction(Account_Number, fDate, toDate);
                  System.out.println("----------------------------------------------------");
                  //System.out.println("Type     Amount     Balance      TransactionDate");
                  for (int i=0; i<statementList.size(); i++) {
	      				Transaction element = statementList.get(i);
	      				System.out.println(element.toString());
	      				//System.out.println(element.getTransactionType()+"      " + element.getTransactionAmount()+"      " + element.getUpToDateBalance() +"      " + element.getTransactionDate());
	      				System.out.println("----------------------------------------------------");
	      		  }
                  //System.out.println("----------------------------------------------------");
                  break;
               default:
                   System.out.println("Invalid Operation");
            }
         }

	
	}
}
