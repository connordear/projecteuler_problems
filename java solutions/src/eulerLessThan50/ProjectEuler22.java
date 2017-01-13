package eulerLessThan50;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Iterator;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;

//Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over 
//five-thousand first names, begin by sorting it into alphabetical order. 
//Then working out the alphabetical value for each name, multiply this value by its alphabetical 
//position in the list to obtain a name score.
//
//For example, when the list is sorted into alphabetical order, 
//COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
//So, COLIN would obtain a score of 938 × 53 = 49714.
//
//What is the total of all the name scores in the file?

public class ProjectEuler22 {
	
	public static void main(String[] args) throws FileNotFoundException
	{
		//System.out.println("Your value is: "+ alphabeticalValue("COLIN"));
		TreeSet<String> names = new TreeSet<String>();
		Scanner input = new Scanner(new File("p022_names.txt"));
		input.useDelimiter(",");
		while(input.hasNext())
		{
			String currentName = input.next().replaceAll( "\"", " ").trim();
			names.add(currentName);

		}
		int runningValue = 0;
		Iterator<String> it = names.iterator();
		int count = 1;
		while(it.hasNext())
		{
			int placeValue = count * (alphabeticalValue(it.next()));
			runningValue += placeValue;
			count ++;
		}
		System.out.println(names);
		System.out.println(runningValue);
		input.close();
	}
	
	public static int alphabeticalValue(String name)
	{
		TreeMap<String, Integer> alphabet = new TreeMap<String, Integer>();
		alphabet.put("A", 1);
		alphabet.put("B", 2);
		alphabet.put("C", 3);
		alphabet.put("D", 4);
		alphabet.put("E", 5);
		alphabet.put("F", 6);
		alphabet.put("G", 7);
		alphabet.put("H", 8);
		alphabet.put("I", 9);
		alphabet.put("J", 10);
		alphabet.put("K", 11);
		alphabet.put("L", 12);
		alphabet.put("M", 13);
		alphabet.put("N", 14);
		alphabet.put("O", 15);
		alphabet.put("P", 16);
		alphabet.put("Q", 17);
		alphabet.put("R", 18);
		alphabet.put("S", 19);
		alphabet.put("T", 20);
		alphabet.put("U", 21);
		alphabet.put("V", 22);
		alphabet.put("W", 23);
		alphabet.put("X", 24);
		alphabet.put("Y", 25);
		alphabet.put("Z", 26);
		
		int alphaVal = 0;
		for(int i = 0; i < name.length(); i++)
		{
			String letter = name.substring(i, i+1);
			alphaVal += alphabet.get(letter);
			//System.out.println(letter);
		}
		return alphaVal;
	}
	

}
