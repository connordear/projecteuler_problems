package eulerLessThan50;

import java.util.Arrays;

//A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
//
//012   021   102   120   201   210
//
//What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

public class ProjectEuler24 {
	
	public static boolean nextPermutation(int[] a)
	{
		//Find longest set inside current permutation that is decreasing
		int headOfSet = a.length - 1;
		while(a[headOfSet] <= a[headOfSet - 1])
		{
			headOfSet--;
		}
		//System.out.println(headOfSet);
		// Now i is the index where the longest decreasing set begins
		// The index beside it is the one we need to switch 
		int pivot = headOfSet - 1;
		//System.out.println(pivot);
		// Now find the largest index with a value larger than j.
		int largestInSet = a.length - 1;
		while(a[largestInSet] < a[pivot])
		{
			largestInSet--;
		}
		
		int hold = a[pivot];
		a[pivot] = a[largestInSet];
		a[largestInSet] = hold;
		int lengthOfSubSet = (a.length) - headOfSet;

		int count = 1;


			for(int go = 0; go < lengthOfSubSet/2; go++)
			{
				int hold2 = a[headOfSet + go];
				a[headOfSet + go] = a[a.length - count];
				a[a.length - count] = hold2;
				count ++;
			}

		
		return true;
	}

	public static void main(String[] args) 
	{
		int [] array = {0,1,2,3,4,5,6,7,8,9};
		System.out.println(Arrays.toString(array));
		int counter = 1;
		while(counter < 1000000)
		{
			nextPermutation(array);
			counter++;

		}
		System.out.println(Arrays.toString(array));
	}

}
