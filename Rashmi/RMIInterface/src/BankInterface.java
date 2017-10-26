import java.rmi.Remote;


public interface BankInterface extends Remote{
	public int add(int x,int y) throws Exception;
}
