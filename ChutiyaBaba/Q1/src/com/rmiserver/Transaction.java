package com.rmiserver;
import java.io.Serializable;
import java.text.DecimalFormat;
import java.util.Date;
public class Transaction implements Serializable {
	private static final long serialVersionUID = -6841131027488692403L;
	
	// decimal formatting to 2 decimal places
	private DecimalFormat precision2 = new DecimalFormat("0.00");
	
	private String transactionType;
	private double transactionAmount;
	private double upToDateBalance;
	private Date transactionDate;
	
	public Transaction(String transactionType, double transactionAmount, double upToDateBalance){
		this.setTransactionType(transactionType);
		this.setTransactionAmount(transactionAmount);
		this.setUpToDateBalance(upToDateBalance);
		transactionDate = new Date();
	}
	
	public String toString() {
		return "Type: " + transactionType +
				"\nAmount: ₹" + precision2.format(transactionAmount) +
			    "\nBalance: ₹" + precision2.format(upToDateBalance) +
			    "\nDate: " + transactionDate.toString() + "\n";
	}
	public String getTransactionType() {
		String type = transactionType;
		return type;
	}

	public Date getTransactionDate() {
		Date date = transactionDate;
		return date;
	}
	
	public double getUpToDateBalance() {
		double balance = upToDateBalance;
		return balance;
	}
	
	public void setUpToDateBalance(double upToDateBalance) {
		this.upToDateBalance = upToDateBalance;
	}

	public void setTransactionDate(Date transactionDate) {
		this.transactionDate = transactionDate;
	}
	public void setTransactionType(String transactionType) {
		this.transactionType = transactionType;
	}

	public double getTransactionAmount() {
		return transactionAmount;
	}

	public void setTransactionAmount(double transactionAmount) {
		this.transactionAmount = transactionAmount;
	}





}
