package com.rmiserver;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.Date;
import java.util.Hashtable;
import java.util.List;
import java.util.Scanner;
import java.util.Base64;

import com.rmiinterface.RMIinterface;

public class ServerOperations extends UnicastRemoteObject implements RMIinterface{
	private static final long serialVersionUID = 1L;
	protected ServerOperations() throws RemoteException {
		super();
	}
	Scanner sc=new Scanner(System.in);
	
	static int Key;
	@Override
	public int GenerateKey(int Ya) throws RemoteException{
		System.out.println("Please enter a Random Number:");
		int Xb = sc.nextInt();
		int Yb=(int)((Math.pow(3,Xb))%17);
		Key =(int)((Math.pow(Ya,Xb))%17);
		System.out.println("Key Generated is: "+Key);
		return Yb;
	}
	static String key = Integer.toString(Key), response;
	
	public static String  encode_decode(String s){
		//System.out.println("---------------------------------");
		String key = Integer.toString(Key);
		//System.out.println("String "+s+ " Key: " + Key + " And converted " + key);
		
		//System.out.println("---------------------------------");
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < s.length(); i++)
		    sb.append((char)(s.charAt(i) ^ key.charAt(i % key.length())));
		String result = sb.toString();
	    System.out.println(result);
	    return result;
	}
	
	
	   @Override
	   public String Primality_Test(String string) throws RemoteException{
		   string = encode_decode(string);
		   int num = Integer.parseInt(string);
	       if (num%2==0) {
	         return encode_decode("Number: "+num+" is Not Prime Number it divisible by: "+ 2);
	       }
	       //if not, then just check the odds
	       else{
	          for(int i=3;i*i<=num;i+=2) {
	              if(num%i==0)
	               return encode_decode("Number: "+num+" is Not Prime Number it divisible by: "+ i);
	          }
	       }
	       return encode_decode("Number: "+num+" is Prime Number");
	   }
	   @Override
	   public String Palindrome(String string) throws RemoteException{
		   string = encode_decode(string);
		   String reverse = new StringBuffer(string).reverse().toString();
	       if (string.equals(reverse))
	         return encode_decode("The String: "+string+" is a Palindrome!!");
	    
	       else
	         return encode_decode("The String: "+string+" is not a Palindrome!!");
	   }
	   @Override
	   public String Fibonacci(String string) throws RemoteException{
		   string = string;
		   int num = Integer.parseInt(string);
		    int[] array = new int[num+1];
	        int a = 0, b = 1, c=1;
	        if(num==1){
	         return encode_decode("The nth Fibonacci number is: 0");
	        }
	        if(num == 2 || num==3)
	        {
	         return encode_decode("The nth Fibonacci number is: 1");
	        }
	        for(int i=3; i <=num; i++){
	            //array[i] = array[i-1] + array[i-2];
	         c = a+b;
	         a = b;
	         b = c;
	        }
	        return "The nth Fibonacci number is: "+ c;
	   }
	   @Override
	   public String lowToupperTolow(String string) throws RemoteException{
		   //System.out.println("Client: " + string);
		   string = encode_decode(string);
		  // System.out.println("Client: After encoding " + string);
	       StringBuilder builder = new StringBuilder();
	        for(int i=0;i<string.length();i++){
	            char stringChar = string.charAt(i);

	            if(92 <= stringChar && stringChar <=122){
	                stringChar = (char)( (stringChar - 32) ); 
	                builder.append(stringChar);
	            }
	            else if (65 <= stringChar && stringChar<=90)
	            {
	               stringChar = (char)( (stringChar + 32) );
	                builder.append(stringChar);
	            }
	        }
	        if(builder.length() == 0){
	            builder.append(string);
	        } 
	        return encode_decode("The Given String is: "+string+" and the change is: "+ builder);
	   }

	
	public static void main(String[] args){
		try {
			LocateRegistry.createRegistry(2020);
			Naming.rebind("//localhost:2020/Server", new ServerOperations());            
            System.err.println("[Server Ready]");
    		
        } catch (Exception e) {
        	System.err.println("Server exception: " + e.toString());
          e.printStackTrace();
        }
	}
	
}
