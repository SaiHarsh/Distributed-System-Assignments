import java.rmi.*;
import java.util.Scanner;  
public class MS20172114_Client
{
	public static void main(String[] args) throws Exception
	{
		MS20172114_Interface query_object=(MS20172114_Interface)Naming.lookup("//localhost:1234/Server");
		Scanner sc=new Scanner(System.in);  


		System.out.println("Welcome to Distributed Banking System");
		System.out.println();
		System.out.println("Enter your Choice:");
		System.out.println("\t1. Deposit Money");
		System.out.println("\t2. Withdraw Money");
		System.out.println("\t3. Check Balance");
		System.out.println("\t4. Mini Statemnt");
		int choice=sc.nextInt();
		if (choice==1) 
		{

			System.out.print("Enter a Account Number: ");
			int acc_num=sc.nextInt();  

			System.out.print("Enter a Amount: ");
			int amount=sc.nextInt();

			String ack=query_object.deposit(acc_num,amount);
			System.out.println(ack);

		}  

		else if (choice==2) 
		{

			System.out.print("Enter a Account Number: ");
			int acc_num=sc.nextInt();  

			System.out.print("Enter a Amount: ");
			int amount=sc.nextInt();

			String ack=query_object.withdraw(acc_num,amount);
			System.out.println(ack);


		}  

		else if (choice==3) 
		{

			System.out.print("Enter a Account Number: ");
			int acc_num=sc.nextInt();  

			int balance=query_object.checkBalance(acc_num);

			System.out.println("Balance available in "+acc_num+" is Rs "+balance+"/-");

		}  
		else if(choice==4)
		{

			System.out.print("Enter a Account Number: ");
			int acc_num=sc.nextInt();  

			System.out.print("Choose an option:\n\t1. Total Summary\n\t2. Summary for some period\n");
			int summary_choice=sc.nextInt();
			if(summary_choice==1)
			{
				String transactDetails=query_object.transaction_details(acc_num);
				System.out.print("Transaction Details:\n"+transactDetails );				
			}  
			else if(summary_choice==2)
			{
				System.out.println("Please follow this format:\n\tYYYY-MM-DD\n\tEx:2017-09-10");
				System.out.print("Enter a Start Date: ");
				String startDate=sc.next();  

				System.out.print("Enter a End Date: ");
				String endDate=sc.next();

				String transactDetails = query_object.transaction_details(acc_num, startDate, endDate);
				System.out.print("Transaction Details:\n"+transactDetails );
			}		
		}	


	}
}
