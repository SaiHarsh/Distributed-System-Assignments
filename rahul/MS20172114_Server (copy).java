import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;     
import java.rmi.Naming;
import java.io.*;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.net.MalformedURLException;


class Serialization
{
	public  String Name;
	public	String RollNum;
	public	List<String> CourseName  = new ArrayList<>();
	public	List<String> CourseScore = new ArrayList<>();

	public Serialization(String Name,String RollNum) 
	{
		this.Name = Name;
		this.RollNum = RollNum;
	}

	public void addCourse(String CourseName)
	{
		this.CourseName.add(CourseName);
	}

	public String getCourseName(int index)
	{
		try
		{
			return CourseName.get(index);
		}
		catch (Exception exception)
		{
			return "-1";
		}
	}
	public void addCourseScore(String CourseScore)
	{
		this.CourseScore.add(CourseScore);
	}
	public String getCourseScore(int index)
	{
		try
		{
			return CourseScore.get(index);
		}
		catch (Exception exception)
		{
			return "";
		}
	}

} 
public class MS20172114_Server  extends UnicastRemoteObject implements MS20172114_Interface 
{

	int index = 0;
	protected MS20172114_Server() throws RemoteException 
	{
		super();
		//
	}

	PrintWriter inpTXTFileWrite;

	public void setFilePath() throws java.io.IOException, FileNotFoundException
	{
		inpTXTFileWrite = new PrintWriter("InterfaceText", "UTF-8");		
	}

	public void beginReadingFile(String str) throws RemoteException
	{
		inpTXTFileWrite.println(str);
	}

	public void endReadingFile() throws RemoteException
	{
		inpTXTFileWrite.close();
	}

	PrintWriter outTXTFileWrite;
	List<Serialization> deSerializer = new ArrayList<Serialization>();
    public void JSONToTXTFile() throws RemoteException 
    {
    	try
    	{
    		outTXTFileWrite = new PrintWriter("JSONToTXTFile.txt", "UTF-8");
    		File file = new File("TXTFileToJSON.json");
	    	Scanner inputFile = new Scanner(file);
	    	index = 0;
	    	int j;
			while (inputFile.hasNext())
				outTXTFileWrite.print(inputFile.nextLine().replaceAll("\\}","").replaceAll("\\{","").replaceAll("\\[","").replaceAll("\\]","").replaceAll("\"Name\"\\:", "\n").replaceAll("\"CourseScore\"", "").replaceAll("\"CourseName\"", "").replaceAll("\"CourseMarks\"", "").replaceAll("\"RollNo\"", "").replaceAll(",", "").replaceAll("\"\\:\\:", ":").replaceAll("\"", ""));
			outTXTFileWrite.close();
			String line;
			file = new File("JSONToTXTFile.txt");
			FileReader fileReader = new FileReader(file);
			BufferedReader readerBuffer = new BufferedReader(fileReader);
			readerBuffer.readLine();
			while ((line = readerBuffer.readLine()) != null)
			{

				int i;
				StringBuilder stringBuilder;
				stringBuilder = new StringBuilder();
				
				for (i=0; i<line.length(); i++) 
					if(line.charAt(i)!=':')
						stringBuilder.append(line.charAt(i));
					else
						break;
				

				String Name = stringBuilder.toString();
				stringBuilder = new StringBuilder();
				
				j = line.length()-1;
				for (; j>0; j--)
					if(line.charAt(j)!=':')
						stringBuilder.append(line.charAt(j));
					else
						break;
				
				int len = j;
				
				stringBuilder.reverse();
				String RollNum = stringBuilder.toString();

				Serialization item = new Serialization(Name, RollNum);
				deSerializer.add(item);

				stringBuilder = new StringBuilder();
				
				int flag = 0;
				for (i=i+1; i<len; i++) 
					if(line.charAt(i)==':' && flag==0)
					{
						deSerializer.get(index).addCourseScore(stringBuilder.toString());
						stringBuilder = new StringBuilder();
						flag = 1;
					}
					else if(line.charAt(i)==':' && flag==1)
					{
						deSerializer.get(index).addCourse(stringBuilder.toString());
						stringBuilder = new StringBuilder();
						flag = 0;
					}
					else
						stringBuilder.append(line.charAt(i));

				try
				{
					deSerializer.get(index).addCourse(stringBuilder.toString());
				}
				finally
				{
					//
				}
				index++;
			}
			inputFile.close();
	    	outTXTFileWrite = new PrintWriter("JSONToTXTFile.txt", "UTF-8");
	    }
	    catch (IOException exception)
	    {
	    	System.out.println("[Opening File ERROR]");
	    }
        for(int i=0;i<index;i++)
        {
        	Serialization iterator = deSerializer.get(i);
			String tempString = iterator.Name + "," + iterator.RollNum +":";
        	for(int j=0;j<iterator.CourseScore.size()-1;j++)
        		tempString += iterator.getCourseName(j) +","+ iterator.getCourseScore(j) +":";
        	int CourseScoreSize=iterator.CourseScore.size()-1;
		
		        if(iterator.getCourseScore(CourseScoreSize).length() > 0)
		        	tempString += iterator.getCourseName(CourseScoreSize) +","+ iterator.getCourseScore(CourseScoreSize);
        		else
        			tempString += "";
        		
        		outTXTFileWrite.print(tempString);
        		outTXTFileWrite.print("\n");
        }
        outTXTFileWrite.close();	
			System.out.println("Converted JSON File to Text File");
			System.out.println("File Generated: JSONToTXTFile.txt");
    }

	PrintWriter outJSONFileWrite;
	List<Serialization> serializer = new ArrayList<Serialization>();
	public void TXTFileToJSON() throws RemoteException
	{
		try
		{
			File file = new File("InterfaceText");
			Scanner inputFile = new Scanner(file);

			while (inputFile.hasNext())
			{
				String inputNextline = inputFile.nextLine();
				
				int i;
				StringBuilder stringBuilder = new StringBuilder();
				
				for (i=0 ; i<inputNextline.length(); i++)
					if(inputNextline.charAt(i)!=',')
						stringBuilder.append(inputNextline.charAt(i));
					else
						break;

				String name = stringBuilder.toString();
				stringBuilder = new StringBuilder();
				
				for (i=i+1; i<inputNextline.length(); i++) 
					if(inputNextline.charAt(i)!=':')
						stringBuilder.append(inputNextline.charAt(i));
					else
						break;

				String RollNum = stringBuilder.toString();

				Serialization tempObject = new Serialization(name, RollNum);
				serializer.add(tempObject);

				stringBuilder = new StringBuilder();
				
				for (i=i+1; i<inputNextline.length(); i++) 
					if(inputNextline.charAt(i)==':')
					{
						serializer.get(index).addCourseScore(stringBuilder.toString());
						stringBuilder = new StringBuilder();
					}
					else if(inputNextline.charAt(i)==',')
					{
						serializer.get(index).addCourse(stringBuilder.toString());
						stringBuilder = new StringBuilder();
					}
					else
						stringBuilder.append(inputNextline.charAt(i));

				try
				{
					serializer.get(index).addCourseScore(stringBuilder.toString());
				}
				finally
				{
					//
				}	
				index ++;
			}
			inputFile.close();
		}
		
		catch (FileNotFoundException exception)
		{
			System.out.println("[File Not Found ERROR]");
		}



		try
		{
			outJSONFileWrite = new PrintWriter("TXTFileToJSON.json", "UTF-8");
		}
		catch(IOException exception)
		{
			System.out.println("[Opening File ERROR]");
		}

		outJSONFileWrite.print("[");		
		for(int i=0;i<index;i++)
		{
			
			Serialization iterator = serializer.get(i);
			String tempString = "{\"Name\":\""+ iterator.Name + "\",\"CourseMarks\":[";
			
			for(int j=0;j<iterator.CourseScore.size()-1;j++)
				tempString += "{\"CourseScore\":"+ iterator.getCourseScore(j) +",\"CourseName\":\""+ iterator.getCourseName(j)+"\""+ "},";


			int CourseScoreSize=iterator.CourseScore.size()-1;

			if(i!=(index-1))
				if(iterator.getCourseScore(CourseScoreSize).length() > 0)
					tempString += "{\"CourseScore\":"+ iterator.getCourseScore(CourseScoreSize) +",\"CourseName\":\""+ iterator.getCourseName(CourseScoreSize)+"\""+ "}],"+ "\"RollNo\":"+ iterator.RollNum+"},";
				else
					tempString += "],"+ "\"RollNo\":"+ iterator.RollNum +"},";

			else
				if(iterator.getCourseScore(CourseScoreSize).length() > 0)
					tempString += "{\"CourseScore\":"+ iterator.getCourseScore(CourseScoreSize) +",\"CourseName\":\""+ iterator.getCourseName(CourseScoreSize)+"\""+ "}],"+ "\"RollNo\":"+ iterator.RollNum+"}";
				else
					tempString += "],"+ "\"RollNo\":"+ iterator.RollNum +"}";
				

			outJSONFileWrite.print(tempString);
		}
		outJSONFileWrite.print("]\n");
		outJSONFileWrite.close();	
	
		System.out.println("Converted Text File to JSON File");
		System.out.println("File Generated: TXTFileToJSON.json");

	}



	public static void main(String[] args) throws Exception
	{
			java.rmi.registry.LocateRegistry.createRegistry(6050);
			MS20172114_Server fileObject = new MS20172114_Server();
			Naming.rebind("//localhost:6050/MS20172114Server", fileObject);
			fileObject.setFilePath();
			System.out.println("[[[Server has been Started]]]");
	}	
}
