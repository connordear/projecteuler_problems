// Starting in the top left corner of a 2x2 grid, and only being able to move
// to the right and down, there are exactly 6 routes to the bottom right corner.// How many such routes are there through a 20x20 grid?
#include <stdio.h>
int main(void)
{
	// Create 20x20 array with each slot filled with a pointer pointing to
	// the slot underneath it. If it's pointing to nothing then it points
	// right. If the pointer points to a node beneath it that is pointing
	// to the right, then on the next iteration it too will point to the
	// right.
	
	int *ptr_array[20][20];
	for(int i = 0; i < 20; i++)
	{
		for(int j = 0; j < 20; j++)
		{	
			int *ptr_right = ptr_array[i + 1][j];
			int *ptr_down = ptr_array[i][j + 1];
			if(i == 19 && j == 19)
			{
				ptr_array[i][j] = (int*)1;
			}
			else if(i == 19 && j < 19)
			{
				ptr_array[i][j] = ptr_down;
			}
			else if(i < 19 && j == 19)
			{
				ptr_array[i][j] = ptr_right;
			}
			else
			{
				ptr_array[i][j] = ptr_down;
			}
		}
	}
	printf("The value of slot 19,5 in the array is: %d.\n", (int)ptr_array[19][5]);

	return 0;	
}
