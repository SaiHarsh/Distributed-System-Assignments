package com.rmiserver;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Account {		
		private int accountNum;
		private String accountName;
		private double balance;
		private String ContactInfo;
		private List<Transaction> transactions; // transactions associated with this account object
	
		// constructor for type Account
		public Account (int accountNum, String accountName, double openingBalance, String contactInfo) {
			this.accountNum = accountNum;
			this.accountName = accountName;
			this.balance = openingBalance;
			this.ContactInfo = contactInfo;
			transactions = new ArrayList<Transaction>();
		}
		
		// add an object of type transaction to the list of transactions
		public void addTransaction(String type, double amount) {
			Transaction e = new Transaction(type, amount, getBalance()); 
			System.out.println("Transaction: " + e);
			System.out.println("Transaction: " + e.getTransactionDate());	
			
			transactions.add(e);
		}
		
		// return all transactions 
		public List<Transaction> getTransactions() {
			return transactions;
		}
		
		// return all transactions within a specified date range
		public List<Transaction> getTransactionsByDate(Date fromDate, Date toDate) {
			
			List<Transaction> statementList = new ArrayList<Transaction>();
			System.out.println("From Date:" + toDate);
			for (int i=0; i<transactions.size(); i++) {
				Transaction element = transactions.get(i);
				
				// check if the date value falls between the specified range 
				System.out.println("getTransactionDate Date:" + element.getTransactionDate());
				if (element.getTransactionDate().after(fromDate) && element.getTransactionDate().before(toDate)) {
					System.out.println("From Date:" + element.getTransactionDate());
					statementList.add(element); 
				}
			}
			return statementList;
		}
	
		public int getAccountNum() {
			return accountNum;
		}
	
		public void setAccountNum(int accountNum) {
			this.accountNum = accountNum;
		}
	
		public double getBalance() {
			return balance;
		}
	
		public void setBalance(double balance) {
			this.balance = balance;
		}
	
		public String getAccountName() {
			return accountName;
		}
	
		public void setAccountName(String accountName) {
		this.accountName = accountName;
	}
	}

