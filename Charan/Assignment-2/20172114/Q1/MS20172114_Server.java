import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.LocateRegistry;
import java.util.Date;
import java.text.ParseException;
import java.text.SimpleDateFormat;
class Customer 
{
		 private String name;
		 private int acc_num;
		 private String acc_type;
		 private int balance;
		 private String contactInfo;
		 private int num_of_transactions;

		 private int[] transactionID = new int[100];
		 private String[] depositORwithdraw = new String[100];
		 private int[] preBalance = new int[100];
		 private int[] postBalance= new int[100];
		 private int[] amount= new int[100];
		 private String[] dateOfTransaction= new String[100];
		

		public Customer(String name, int acc_num, String acc_type, int balance, String contactInfo,int num_of_transactions) 
		{
			this.name = name;
			this.acc_num = acc_num;
			this.acc_type = acc_type;
			this.balance = balance;
			this.contactInfo=contactInfo;
			this.num_of_transactions=num_of_transactions;
		}

		 public String getName() { return name; }
		 public int getAcc_num() { return acc_num; }
		 public String getAcc_type() { return acc_type; }
		 public int getBalance() { return balance; }
		 public String getContactInfo() { return contactInfo; }

		 public void setBalance(int balance) { this.balance=balance; }
		 public void appendTransaction(int ttransactionID,String tdepositORwithdraw,int tamount,int tpreBalance,int tpostBalance,String tdateOfTransaction)
		 {
		 //	System.out.println("Came Here "+ num_of_transactions);
			transactionID[num_of_transactions]=ttransactionID;
			depositORwithdraw[num_of_transactions]=tdepositORwithdraw;
			preBalance[num_of_transactions]=tpreBalance;
			amount[num_of_transactions]=tamount;
			postBalance[num_of_transactions]=tpostBalance;
			dateOfTransaction[num_of_transactions]=tdateOfTransaction;
			num_of_transactions=num_of_transactions+1;

			//System.out.println(depositORwithdraw[num_of_transactions-1] + preBalance[num_of_transactions-1]+postBalance[num_of_transactions-1]+dateOfTransaction[num_of_transactions-1]);

		 }
		 public String printTransDetails()
		 {	
			String tDetails="Transaction ID\tDate\t\tWithdraw/Deposit\tAmount\tPre-Balance\tPost-Balance\n";
			for (int i=0; i<num_of_transactions;i++ ) 
			{
				tDetails=tDetails + transactionID[i]+ "\t\t"+dateOfTransaction[i].toString()+ "\t" + depositORwithdraw[i]+"\t\t"+amount[i]+"\t"+ preBalance[i]+"\t\t"+postBalance[i]+"\n";
			}
			return tDetails;
		 }
		 public String printTransDetails(String startDate,String endDate) throws ParseException
		 {	


	        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
	        Date date1 = sdf.parse(startDate);
	        Date date2 = sdf.parse(endDate);
	        /*
	        Date dateMain =sdf.parse(dateOfTransaction[0]);
	            System.out.println("date1 : " + sdf.format(date1));
				System.out.println("dateMain : " + sdf.format(dateMain));*/
	       /* if(date1.compareTo(dateMain) == 0)
	        {
	        	System.out.println("Same");
	        }*/
		 	String tDetails="Date\t\t\t\tWithdraw/Deposit\tAmount\tPre-Balance\tPost-Balance\n";
			for (int i=0; i<num_of_transactions;i++ ) 
			{
				if (((date1.compareTo(sdf.parse(dateOfTransaction[i])) > 0) && (date2.compareTo(sdf.parse(dateOfTransaction[i])) < 0))||(date1.compareTo(sdf.parse(dateOfTransaction[i])) == 0)||(date2.compareTo(sdf.parse(dateOfTransaction[i])) == 0))
					tDetails=tDetails+ dateOfTransaction[i].toString()+ "\t" + depositORwithdraw[i]+"\t\t"+amount[i]+"\t"+ preBalance[i]+"\t\t"+postBalance[i]+"\n";
			}
			return tDetails;
		 }
}

class Queries extends UnicastRemoteObject implements MS20172114_Interface
{

	public Customer[] customer=new Customer[100];
	public int transactionID;


	public Queries() throws Exception
	{
				transactionID=0;
				customer[1] = new Customer("Customer_1",201700001,"Basic",5000,"127.0.0.1000",0);
				customer[2] = new Customer("Customer_2",201700002,"Basic",5000,"127.0.0.1000",0);
				customer[3] = new Customer("Customer_3",201700003,"Premium",5000,"127.0.0.1000",0);
				customer[4] = new Customer("Customer_4",201700004,"Basic",5000,"127.0.0.1000",0);
				customer[5] = new Customer("Customer_5",201700005,"Basic",5000,"127.0.0.1000",0);
				customer[6] = new Customer("Customer_6",201700006,"Premium",5000,"127.0.0.1000",0);
				customer[7] = new Customer("Customer_7",201700007,"Basic",5000,"127.0.0.1000",0);
				customer[8] = new Customer("Customer_8",201700008,"Premium",5000,"127.0.0.1000",0);
				customer[9] = new Customer("Customer_9",201700009,"Premium",5000,"127.0.0.1000",0);
				customer[10] = new Customer("Customer_10",201700010,"Premium",5000,"127.0.0.1000",0);
	}


	public String deposit(int acc_num,int amount)
	{
		transactionID=transactionID+1;
		int id= acc_num-201700000;
		int preBalance=customer[id].getBalance() ;
		customer[id].setBalance(preBalance + amount);
		
		Date date = new Date();
		String modifiedDate= new SimpleDateFormat("yyyy-MM-dd").format(date);

		customer[id].appendTransaction(transactionID,"Deposit\t",amount,preBalance,customer[id].getBalance(),modifiedDate);
		
			String ack;
			ack= "You have successfully deposited "+ amount + "/- with Transaction-ID:" +transactionID+"\n"+"Your Current Account Balance is "+customer[id].getBalance();
			return ack;	
	}

	public String withdraw(int acc_num,int amount)
	{
		transactionID=transactionID+1;
		int id= acc_num-201700000;
		if(customer[id].getBalance() >= amount)
		{		
			int preBalance=customer[id].getBalance() ;
			customer[id].setBalance(preBalance - amount);
		
			Date date = new Date();
			String modifiedDate= new SimpleDateFormat("yyyy-MM-dd").format(date);

			customer[id].appendTransaction(transactionID,"Withdraw",amount,preBalance,customer[id].getBalance(),modifiedDate);	
			String ack;
			ack= "You have successfully withdrawn "+ amount + "/- with Transaction-ID:" +transactionID+"\n"+"Your Current Account Balance is "+customer[id].getBalance();
			return ack;
		}
		else 
		{
			return "Transaction failed due to Insufficient Balance";	
		}
	}

	public int checkBalance(int acc_num)
	{
		int id= acc_num-201700000;
		return customer[id].getBalance();
	}

	public String transaction_details(int acc_num)
	{
		int id= acc_num-201700000;
		String tDetails=customer[id].printTransDetails();
		return tDetails;
	}
	public String transaction_details(int acc_num, String startDate, String endDate) throws ParseException
	{
		int id= acc_num-201700000;
		String tDetails=customer[id].printTransDetails(startDate,endDate);
		return tDetails;
	}

}
public class MS20172114_Server
{
	public static void main(String a[]) throws Exception 
	{
		LocateRegistry.createRegistry(1234);
		Queries obj= new Queries();
		Naming.rebind("//localhost:1234/Server",obj);
		System.out.println("Server Started");
		
	}
}