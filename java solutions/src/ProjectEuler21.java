import java.util.ArrayList;

//Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
//If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
//
//For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
//
//Evaluate the sum of all the amicable numbers under 10000.
public class ProjectEuler21 {
	
	public static int sumOfDivisors(int a)
	{
		ArrayList<Integer> factors = new ArrayList<Integer>();
		for(Integer i = 1; i <= Math.sqrt(a); i++)
		{
			if(a % i == 0)
			{
				factors.add(i);
				if(a / i < a)
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
		return sum;
	}

	public static void main(String[] args) 
	{
		ArrayList<Integer> amicableNumbers = new ArrayList<Integer>();
		for(int a = 1; a < 10000; a++)
		{
			int b = sumOfDivisors(a);
			if(b < 10000)
			{
				int sumDivB = sumOfDivisors(b);
				if(sumDivB == a && b != a)
				{
					System.out.printf("The numbers %d and %d are amicable numbers.\n", a, b);
					if(!amicableNumbers.contains(a))
					{
						amicableNumbers.add(a);
					}
					if(!amicableNumbers.contains(b))
					{
						amicableNumbers.add(b);
					}
				}
			}
		}
		int sumOfAmicable = 0;
		for(int l = 0; l < amicableNumbers.size(); l++)
		{
			sumOfAmicable += amicableNumbers.get(l);
		}
		System.out.printf("The sum of all amicable numbers below 10000 is %d\n", sumOfAmicable);

	}

}
