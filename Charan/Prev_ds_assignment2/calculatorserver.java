package ds_assignment2;

import java.rmi.Naming; 
public class calculatorserver 
{ 
	calculatorserver() 
	{ 
		try 
		{ 
			calculatorimple c = new calculatorimple(); 
			Naming.rebind("RMI://127.0.0.1:1020/CalculatorService", c); 
		} 
		catch (Exception e) 
		{ 
			e.printStackTrace(); 
		} 
	}
	public static void main(String[] args) 
	{ 
		new calculatorserver(); 
	} 
}	