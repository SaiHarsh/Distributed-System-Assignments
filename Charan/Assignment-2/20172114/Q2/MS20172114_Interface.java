import java.rmi.*;
public interface MS20172114_Interface extends Remote
{
	public String primalityTest(String n) throws Exception;
	public String palindromeTest(String palString) throws Exception;
	public String nthFibonacci(String n) throws Exception;
	public String stringCaseConverter(String string) throws Exception;
	
	public int shareKey(int key) throws Exception ;

}