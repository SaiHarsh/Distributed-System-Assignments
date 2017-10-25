import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.LocateRegistry;
import java.util.Date;
import java.text.ParseException;
import java.util.Random;  

class Functionalities extends UnicastRemoteObject implements MS20172114_Interface
{

	static String keyString;
	
	public Functionalities() throws Exception
	{
		super();
	}


	public int shareKey(int receivedSecretKey) throws Exception 
	{

		Random rand = new Random();
		int privateKey = rand.nextInt(10) + 1;

		int sharedSecretKey=(int)((Math.pow(3,privateKey))%17);
		int mainKey =(int)((Math.pow(receivedSecretKey,privateKey))%17);
		keyString = Integer.toString(mainKey);

		//System.out.println(privateKey+" Generated Key: "+key);

		return sharedSecretKey;
	}

	private static String dhkeEncrypt(String string)
	{
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < string.length(); i++)
			sb.append((char)(string.charAt(i) ^ keyString.charAt(i % keyString.length())));
		String encryptedMessage = sb.toString();
		return encryptedMessage;
	}
	private static String dhkeDecrypt(String string)
	{
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < string.length(); i++)
			sb.append((char)(string.charAt(i) ^ keyString.charAt(i % keyString.length())));
		String decryptedMessage = sb.toString();
		return decryptedMessage;
	}



	private int isPrime(int n)
	{
		if (n <= 1)  return 0;
		if (n <= 3)  return 1;
		if (n%2 == 0 || n%3 == 0) return 0;
		for (int i=5; i*i<=n; i=i+6)
			if (n%i == 0 || n%(i+2) == 0)
				return 0;
		return 1;
	}
	public String primalityTest(String number) throws Exception
	{	
		int num = Integer.parseInt(dhkeDecrypt(number));
		String messageResponse;
		if(isPrime(num)==1)
			messageResponse="Yes, It's Prime";
		else
			messageResponse="No, It's not Prime";
		return dhkeEncrypt(messageResponse);
	}
	public String palindromeTest(String palString) throws Exception
	{
		String mainString = dhkeDecrypt(palString);

		String reverse = "";
		int length = mainString.length();

		for ( int i = length - 1; i >= 0; i-- )
			reverse = reverse + mainString.charAt(i);
		String messageResponse;
		if (mainString.equals(reverse))
			messageResponse="Yes, It's Palindrome";
		else
			messageResponse="No, It's not Palindrome";

		return dhkeEncrypt(messageResponse);
	}

	private static int fib(int n)
	{
		if (n <= 1)
			return n;
		return fib(n-1) + fib(n-2);
	}
	public String nthFibonacci(String number) throws Exception
	{
		int num = Integer.parseInt(dhkeDecrypt(number));

		String messageResponse = num+" th Fibonacci Number is "+fib(num);
		return dhkeEncrypt(messageResponse);
	}
	public String stringCaseConverter(String string) throws Exception
	{
		String mainString = dhkeDecrypt(string);

		StringBuilder sb = new StringBuilder(mainString);
		for (int index = 0; index < sb.length(); index++) {
			char c = sb.charAt(index);
			if (Character.isLowerCase(c)) {
				sb.setCharAt(index, Character.toUpperCase(c));
			} else {
				sb.setCharAt(index, Character.toLowerCase(c));
			}
		}
		String messageResponse="Case Converted String: "+sb.toString();
		return dhkeEncrypt(messageResponse);
	}

}
public class MS20172114_Server
{
	public static void main(String a[]) throws Exception 
	{
		LocateRegistry.createRegistry(2026);
		Functionalities obj= new Functionalities();
		Naming.rebind("//localhost:2026/Server",obj);
		System.out.println("Server Started");

	}
}
