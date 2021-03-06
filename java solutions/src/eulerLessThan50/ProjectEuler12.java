package eulerLessThan50;

import java.util.ArrayList;

//The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
//
//1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
//We can see that 28 is the first triangle number to have over five divisors.
//
//What is the value of the first triangle number to have over five hundred divisors?
public class ProjectEuler12 {
	
	//Didn't end up needing to resort to checking primes..
//	public static boolean checkPrime(int a)
//	{
//		boolean test = true;
//		for(int i = 2; i <= Math.sqrt(a); i++)
//		{
//			if(a % i == 0)
//			{
//				test = false;
//				break;
//			}
//		}
//		return test;
//	}
	
	//this way is faster
	public static int numOfDivisors2(int a)
	{
		ArrayList<Integer> factors = new ArrayList<Integer>();
		for(Integer i = 1; i <= Math.sqrt(a); i++)
		{
			if(a % i == 0)
			{
				factors.add(i);
				factors.add(a / i);
			}
		}
		//System.out.println(factors);
		return factors.size();
	}
	
	//Too inefficient
//	public static int numOfDivisors(int a)
//	{
//		int num = 0;
//		
//		for(int i = 1; i <= a; i++)
//		{
//			if(a % i == 0)
//			{
//				num ++;
//			}
//		}
//		
//		return num;
//	}

	public static void main(String[] args) 
	{
		//First create a triangle number generator for the first 10 terms
		
		for(int i = 1; i < 11; i++)
		{
			int triangled = 0;
			for(int j = 1; j <= i; j++)
			{
				triangled += j;
			}
			System.out.printf("The %dth triangle number is: " + triangled + ".\n", i);
		}
		
		int testNum = 28;
		int testAns = numOfDivisors2(testNum);
		System.out.printf("The number of divisors in %d is: " + testAns + ".\n", testNum);
		
		//Now make it run until we have a num of divisors > 500.
		

//		int count = 37580115;
//		while(numDivisor < 500)
//		{
//			int triangled = 0;
//			for(int j = 1; j <= count; j++)
//			{
//				triangled += j;
//			}
//			numDivisor = numOfDivisors2(triangled);
//			System.out.printf("The number of divisors in the triangle number %d is %d.\n", triangled, numDivisor);
//			if(numDivisor > 500)
//			{
//				System.out.println("The first triangle number with greater than 500 divisors is: " + triangled);
//			}
//			count ++;
//		}
		int numDivisor = 0;
		int prevTriangled = 0;
		int triangled = 0;
		int count = 1;
		while(numDivisor < 500)
		{
			triangled = prevTriangled + count;
			count++;

			numDivisor = numOfDivisors2(triangled);
			//System.out.printf("The number of divisors in the triangle number %d is %d.\n", triangled, numDivisor);
			if(numDivisor > 500)
			{
				System.out.println("The first triangle number with greater than 5 divisors is: " + triangled + " and the previous value " + prevTriangled);
			}
			prevTriangled = triangled;
		}
		
	}

}
