package ds_assignment2;

import java.rmi.Naming; 
public class calculatorclient 
{ 
	public static void main(String[] args) 
	{ 
		try 
		{ 
			calculatorimple c = (calculatorimple) Naming.lookup("//127.0.0.1:1020/CalculatorService");
			System.out.println("addition : "+c.add(20, 15));
		} 
		catch (Exception e) 
		{ 
			System.out.println(e); 
		} 
	} 
}