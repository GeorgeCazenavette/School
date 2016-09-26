/*********************************************************
Author: 	George Cazenavette and Henry Barham
Instructor:	Dr. Gourd
Class:		CSC 220 001
Assignment: Project Gourd #2
*********************************************************/

import java.util.*;
import java.lang.Math;

public class ProjectGourd2
{
	public static void main(String[] args)
	{
		//stores the input values as a 2D array
		int grid[][] = readNumbers();
		//finds the maximum sum of 4 consecutive values
		int max = findMaxSum(grid);
		//prints the maximum sum
		System.out.println(max);
	}
	
	// reads the 2D array from STDin and returns a 2D array
	private static int[][] readNumbers()
	{
		//creates a scanner object to read in the inputs
		Scanner in = new Scanner(System.in);
		//initializes a 20x20 grid to store the input values
		int inputGrid[][] = new int[20][20];
		//stores each input value in its respective location in the grid
		for (int i = 0; i < 20; i++)
		{
			for (int j = 0; j < 20; j++)
			{
				inputGrid[i][j] = in.nextInt();
			}
		}
		//returns the 20x20 grid
		return inputGrid;
	}
	
	// Finds the maximum sum of 4 consecutive numbers
	// Finds the maximum sum of 4 consecutive numbers
	private static int findMaxSum(int[][] g)
	{
		//initializes variables for the max sum found so far and the current sum
		int maxSum = 0;
		int thisSum;
		//checks every sum in the grid
		for (int i = 0; i < 20; i++)
		{
			//stops at 16 so that the farthest number is in the last column of the grid
			for (int j = 0; j < 17; j++)
			{
				//finds the sum of the 4 consecutive values
				thisSum = g[i][j] + g[i][j + 1] + g[i][j + 2] + g[i][j + 3];
				//stores the current sum as the max sum if it is larger
				if (thisSum > maxSum)
					maxSum = thisSum;
			}
		//returns the max sum found
		}
		return maxSum;
	}
}