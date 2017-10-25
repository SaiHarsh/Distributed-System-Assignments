import java.rmi.*;
import java.rmi.server.*;
import java.util.ArrayList;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

public class Dictionary extends UnicastRemoteObject implements DictionaryInterface{

	private static final long serialVersionUID = 1L;

	Dictionary() throws RemoteException{
		super();
	}
	
	public List<String> query(String word) throws RemoteException{
		List<String> sol = new ArrayList<String>();
		
		try{
			System.setProperty("http.proxyHost", "proxy.iiit.ac.in");
			System.setProperty("http.proxyPort", "8080");
			Document document = Jsoup.connect("http://google-dictionary.so8848.com/meaning?word="+word).get();
			for(Element row : document.select(".std ol li")){
				sol.add(row.text());
			}
			
		} catch(Exception e){
			e.printStackTrace();
		}
		return sol;
	}
}
