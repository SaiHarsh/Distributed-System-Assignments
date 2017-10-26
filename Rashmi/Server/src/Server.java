import java.rmi.Naming;
import java.rmi.server.UnicastRemoteObject;
public class Server extends UnicastRemoteObject implements RMIInterface {
	public static void main(String a[]){
		//Creating Server
		try {
			Naming.rebind("//localhost/MyServer", new ServerOperation());            
            System.err.println("[Server is up]");
            
        } catch (Exception e) {
        	System.err.println("Server exception: " + e.toString());
          e.printStackTrace();
        }
	}

}
