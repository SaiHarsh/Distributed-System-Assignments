import java.rmi.*;
import java.util.Scanner;
import java.util.Random;  
public class MS20172114_Client
{
	static String keyString;

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


	public static void main(String[] args) throws Exception
	{
		MS20172114_Interface query_object=(MS20172114_Interface)Naming.lookup("//localhost:2026/Server");
		Scanner sc=new Scanner(System.in);  


		Random rand = new Random();
		int  privateKey = rand.nextInt(10) + 1;

		int  sharedSecretKey = (int)((Math.pow(3,privateKey))%17);
		int receivedSecretKey = query_object.shareKey(sharedSecretKey);

		int mainKey = (int)((Math.pow(receivedSecretKey,privateKey))%17);
		keyString = Integer.toString(mainKey);

		//System.out.println(privateKey+" Generated Key: "+key);

		System.out.println("Enter your Choice:");
		System.out.println("\t1. Primality Test");
		System.out.println("\t2. Palindrome Test");
		System.out.println("\t3. N​th Fibonacci Number");
		System.out.println("\t4. String case converter​");
		int choice=sc.nextInt();
		if (choice==1) 
		{

			System.out.print("Enter an integer \"n\": ");
			String n=sc.next();  

			String response=query_object.primalityTest(dhkeEncrypt(n));
			System.out.println(dhkeDecrypt(response));

		}  

		else if (choice==2) 
		{

			System.out.print("Enter a String: ");
			String palString=sc.next();  

			String response=query_object.palindromeTest(dhkeEncrypt(palString));
			System.out.println(dhkeDecrypt(response));

		}  

		else if (choice==3) 
		{

			System.out.print("Enter an integer \"n\": ");
			String n=sc.next();  

			String response=query_object.nthFibonacci(dhkeEncrypt(n));
			System.out.println(dhkeDecrypt(response));

		}  
		else if(choice==4)
		{
			System.out.print("Enter a String: ");
			String string=sc.next();  

			String response=query_object.stringCaseConverter(dhkeEncrypt(string));
			System.out.println(dhkeDecrypt(response));
		}	


	}
}
