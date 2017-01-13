package eulerLessThan50;

import java.util.ArrayList;

//A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
//For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
//
//A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
//
//As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
//By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
//However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
//as the sum of two abundant numbers is less than this limit.
//
//Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

public class ProjectEuler23 {
	
	public static boolean isAbundant(int a)
	{
		ArrayList<Integer> factors = new ArrayList<Integer>();
		for(Integer i = 1; i <= Math.sqrt(a); i++)
		{
			if(a % i == 0)
			{
				factors.add(i);
				if(a / i < a && !factors.contains(a / i))
				{
					factors.add(a / i);
				}
			}
		}
		//System.out.println(factors);
		int sum = 0;
		for(Integer j = 0; j < factors.size(); j++)
		{
			sum += factors.get(j);
		}
		//System.out.printf("The sum of the factors of %d is %d.\n", a, sum);
		if(sum > a)
		{
			return true;
		}
		return false;
	}

	public static void main(String[] args) 
	{
		int x = 13;
		if(isAbundant(x))
		{
			System.out.printf("The number %d is an Abundant number.\n", x);
		}
		else
		{
			System.out.printf("The number %d is a deficient number.\n", x);
		} 
		ArrayList<Integer> abundants = new ArrayList<Integer>();
		for(int i = 1; i < 28123; i++)
		{
			if(isAbundant(i))
			{
				abundants.add(i);
			}
		}
		abundants.sort(null);
		System.out.println(abundants);
		ArrayList<Integer> nonSummable = new ArrayList<Integer>();
		int count = 0;
		for(int j = 0; j < 28123; j++)
		{
			int indexHigh = abundants.size() - 1;
			int indexLow = 0;
			int highest = abundants.get(indexHigh);
			int lowest = abundants.get(indexLow);
			
			while(highest >= lowest)
			{
				//System.out.println("highest value = " + highest + " and lowest = " + lowest);
				if(highest + lowest == j)
				{
					System.out.println("found a sum.");
					count ++;
					break;
				}
				else if(highest == lowest)
				{
					nonSummable.add(j);
					System.out.println("There is a non summable integer" + j);
					break;
				}
				else if(highest + lowest < j)
				{
					indexLow ++;
					lowest = abundants.get(indexLow);
					
				}
				else if(highest + lowest > j)
				{
					indexHigh --;
					highest = abundants.get(indexHigh);
				}
				
			}
		}
		
		int finalSum = 0;
		for(int k = 0; k < nonSummable.size(); k++)
		{
			finalSum += nonSummable.get(k);
		}
		System.out.println(count);
		System.out.printf("The final sum of all integers not summable by abundant numbers is %d.\n", finalSum);

	}

}
