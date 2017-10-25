import java.rmi.*;
public interface MS20172114_Interface extends Remote
{
	public String deposit(int acc_num,int amount) throws Exception;
	public String withdraw(int acc_num,int amount) throws Exception;
	public int checkBalance(int acc_num) throws Exception;
	public String transaction_details(int acc_num) throws Exception;
	public String transaction_details(int acc_num, String startDate, String endDate) throws Exception;
}