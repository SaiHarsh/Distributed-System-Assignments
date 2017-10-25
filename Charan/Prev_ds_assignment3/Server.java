import java.rmi.*;
//import java.rmi.registry.*;

public class Server {

	public static void main(String[] args) {
		try{
			DictionaryInterface obj = new Dictionary();		
			Naming.rebind("Try", obj);
		} catch(Exception e){
			e.printStackTrace();
		}

	}

}
