import java.rmi.*;
import java.util.List;
public interface DictionaryInterface extends Remote{
	public List<String> query(String word) throws RemoteException;
}
