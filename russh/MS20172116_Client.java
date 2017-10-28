package com.rmiclient;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.util.Scanner;

import com.rmiinterface.MS20172116_Interface;


public class MS20172116_Client {
	private static MS20172116_Interface look_up;
	static Scanner sc=new Scanner(System.in);
	static String key="";
	public static String encode_decode(String s){
		StringBuilder sb = new StringBuilder();
	    for(int i = 0; i < s.length(); i++)
	        sb.append((char)(s.charAt(i) ^ key.charAt(i % key.length())));
	    String result = sb.toString();
	    return result;
	}
	
	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
		look_up = (MS20172116_Interface) Naming.lookup("//localhost:2020/Server");
		String response, string;
		String num;
		/*Generating Key*/
		System.out.println("Please enter a Random Number:");
		int Xa = sc.nextInt();
		int Ya=(int)((Math.pow(3,Xa))%17);
		int Yb = look_up.GenerateKey(Ya);
		int Key = (int)((Math.pow(Yb,Xa))%17);
		key = Integer.toString(Key);
		System.out.println("Key Generated is:"+key);
		
		while(1 > 0){
				System.out.println("Enter your choice \n P: Primality​ ​ Test \n R: Palindrome​ ​ Test \n N: Nth Fibonacci​ ​ Number \n S: String​ ​ case​ ​ converter​ ​ (upper​ ​ to​ ​ lower​ ​ and​ ​ lower​ ​ to​ ​ upper)");
	            char choose = sc.next().charAt(0);
	            switch(choose) {
            	case 'P':
            		System.out.println("Enter Number of Prime Test");
            		num = sc.next();
            		num = encode_decode(num);
            		response = look_up.Primality_Test(num);
            		response = encode_decode(response);
            		System.out.println("-----------------------------------------------------------------------");
            		System.out.println("[Server:]"+response);
            		System.out.println("-----------------------------------------------------------------------");
            		break;
            	case 'R':
            		System.out.println("Enter String of Palinedrome Test");
            		string = sc.next();
            		string = encode_decode(string);
            		response = look_up.Palindrome(string);
            		response = encode_decode(response);
            		System.out.println("-----------------------------------------------------------------------");
            		System.out.println("[Server:]"+response);
            		System.out.println("-----------------------------------------------------------------------");
            		break;
            	case 'N':
            		System.out.println("Enter the n value");
            		num = sc.next();
            		string = num;
            		System.out.println("-----------------------------------------------------------------------");
            		response = look_up.Fibonacci(num);
            		response = response;
            		System.out.println("[Server:]"+response);
            		System.out.println("-----------------------------------------------------------------------");
            		break;
            	case 'S':
            		System.out.println("Enter String to convert Upper to Lower and Lower to Upper");
            		string = sc.next();
            		string = encode_decode(string);
            		response = look_up.lowToupperTolow(string);
            		response = encode_decode(response);
            		System.out.println("-----------------------------------------------------------------------");
            		System.out.println("[Server:]"+response);
            		System.out.println("-----------------------------------------------------------------------");
            		break;
            	
            }
           }
	}
}

