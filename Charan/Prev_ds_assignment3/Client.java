import java.rmi.*;
import java.util.Scanner;
import java.util.List;
public class Client {

	public static void main(String[] args) {
		try{
			DictionaryInterface access = (DictionaryInterface)Naming.lookup("rmi://localhost/Try");
			System.out.print("Enter the word to get the meaning : ");
			Scanner scan = new Scanner(System.in);
			String word = scan.nextLine();
			scan.close();
			List<String> ans = access.query(word);
			int i = 0;
			while(i < ans.size()){
				System.out.println(ans.get(i));
				i++;
			}
		} catch(Exception e){
			e.printStackTrace();
		}
	}

}
