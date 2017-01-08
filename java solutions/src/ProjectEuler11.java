// Project Euler # 11 : 
// What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
	
public class ProjectEuler11 {

	public static void main(String[] args) throws FileNotFoundException 
	{
		//First build 20x20 array by reading in from a file holding the numbers
		int[][] multi = new int[20][20];
				Scanner input = new Scanner(new File("array.txt"));
		int j = -1;
		while(j < 20)
		{
		for(int i = 0; i < 20; i++)
		{
			System.out.println("i = " + i);
			if(i == 0)
			{
				j++;
				System.out.println("j = " + j);
			}
			if(j == 20)
			{
				break;
			}
			
			if(input.hasNextInt())
			{
				multi[j][i] = input.nextInt();
			}
		

		}
		}
		input.close();
		System.out.println(Arrays.deepToString(multi));
		// Now take the product of each direction of numbers
		int biggestDiagonal = 1;
		int prevDiag = 1;
		//Diagonal Down Search
		for(int m = 0; m < 17; m++)
		{
			for(int n = 0; n < 17; n++)
			{
				int num1 = multi[m][n];
				int num2 = multi[m + 1][n + 1];
				int num3 = multi[m + 2][n + 2];
				int num4 = multi[m + 3][n + 3];
				int prod = num1 * num2 * num3 * num4;
				if(prod > biggestDiagonal)
				{
					prevDiag = biggestDiagonal;
					biggestDiagonal = prod;
				}
			}
		}
		System.out.println("The largest product diagonally is: " + biggestDiagonal + " and the previous was: " + prevDiag);
		//Diagonal up Search
		int biggestDiagonalUp = 1;
				for(int x = 3; x < 20; x++)
				{
					for(int y = 0; y < 17; y++)
					{
						int num1 = multi[x][y];
						int num2 = multi[x - 1][y + 1];
						int num3 = multi[x - 2][y + 2];
						int num4 = multi[x - 3][y + 3];
						int prod = num1 * num2 * num3 * num4;
						if(prod > biggestDiagonalUp)
						{
							biggestDiagonalUp = prod;
						}
					}
				}
				System.out.println("The largest product diagonally up is: " + biggestDiagonalUp);

		//Vertical Search
		int biggestVertical = 1;
		int prevVert = 1;
		for(int p = 0; p < 17; p++)
		{
			for(int q = 0; q < 20; q++)
			{
				int num1 = multi[p][q];
				int num2 = multi[p + 1][q];
				int num3 = multi[p + 2][q];
				int num4 = multi[p + 3][q];
				int prod = num1 * num2 * num3 * num4;
				if(prod > biggestVertical)
				{
					prevVert = biggestVertical;
					biggestVertical = prod;
				}
			}
		}
		System.out.println("The largest product vertically is: " + biggestVertical + " and the previous was: " + prevVert);
		//Horizontal Search
				int biggestHorizontal = 1;
				int prevHorz = 1;
				for(int r = 0; r < 20; r++)
				{
					for(int s = 0; s < 17; s++)
					{
						int num1 = multi[r][s];
						int num2 = multi[r][s + 1];
						int num3 = multi[r][s + 2];
						int num4 = multi[r][s + 3];
						int prod = num1 * num2 * num3 * num4;
						if(prod > biggestHorizontal)
						{
							prevHorz = biggestHorizontal;
							biggestHorizontal = prod;
						}
					}
				}
				System.out.println("The largest product horizontally is: " + biggestHorizontal + " and the previous was: " + prevHorz);
		

	}

}
