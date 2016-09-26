/*********************************************************
Author: 	George Cazenavette and Henry Barham
Instructor:	Dr. Gourd
Class:		CSC 220 001
Assignment: Project Gourd #1
*********************************************************/

import java.util.*;
import java.lang.Math;

public class ProjectGourd1
{
	public static void main(String[] args)
	{
		//calls a function to return a count of all leading numbers
		int numArray[] = readNumbers();
		//calls a function to return an array with the percent composition of each number
		double percents[] = getPercents(numArray);
		//created the table on which the results are displayed
		printTable(numArray, percents);
	}
	
	// reads the list of numbers from STDin and returns an array with the count of each leading digit
	private static int[] readNumbers()
	{
		//Creates a scanner to read from stdin
		Scanner in = new Scanner(System.in);
		//initializes an array to hold a count of each leading number
		int numCount[] = new int[10];
		//initializes an int to hold the current number
		int currentNumber;
		//reads in numbers until there are none left
		while (in.hasNextInt())
		{
			//stores the current number from stdin
			currentNumber = in.nextInt();
			//this loop divides the number by 10 until the leading digit is found (when the number is less than 10)
			while (currentNumber >= 10)
			{
				currentNumber /= 10;
			}
			//increments the corresponding value in the array of leading digits
			numCount[currentNumber]++;
		}
		//returns the array with the total counts of the leading digits
		return numCount;
	}
	
	// calculates and returns an array with the percentage of each leading digit
	private static double[] getPercents(int[] a)
	{
		double sum = 0;
		//finds the total number of numbers
		for (int num : a)
		{
			sum += num;
		}
		double p[] = new double[10];
		//creates an array with each leading digit's percent of the total
		for (int i = 0; i < a.length; i++)
		{
			p[i] = a[i] / sum * 100;
		}
		//returns the array of percents
		return p;
	}
	
	// prints the correctly formatted table
	private static void printTable(int[] a, double[] p)
	{
		//a resuable string of "-" to use in the table
		String bigLine = new String(new char[32]).replace("\0", "-");
		System.out.println(bigLine);
		//column headers
		System.out.println("Leading Digit  Count           %");
		System.out.println(bigLine);
		//spaces in the table
		//the ones that aren't initialized are calculated later
		int space1 = 14;
		int space2;
		int space3 = 10;
		int	space4;
		//initializes sums for the bottom of the table
		int countSum = 0;
		double percentSum = 0;
		String roundedPercentStr;
		for (int i = 0; i < a.length; i++)
		{
			//adds each number's respective value to the count sum and the percent sum
			countSum += a[i];
			percentSum += p[i];
			//creates a String that is the percent rounded to 2 decimal places
			roundedPercentStr = String.format("%.2f", p[i]);
			//This if statement was added to avoid taking the log of 0
			//It uses the lengths of the numbers to calclate the length of the space
			//
			if (a[i] != 0)
				space2 = 16 - (int)(Math.floor(Math.log10((double)a[i])) + 1) - roundedPercentStr.length();
			else
				space2 = 15 - roundedPercentStr.length();
			//prints the row of the table with the numbers and spaces
			System.out.println(i + new String(new char[space1]).replace("\0", " ") + a[i] + new String(new char[space2]).replace("\0", " ") + roundedPercentStr + "%");
		}
		//creates a string of the rounded percent sum
		//should always be 100, calculated to check for errors
		String roundedTotalPercent = String.format("%.2f", percentSum);
		//calculates the length of the space
		space4 = 16 - (int)(Math.floor(Math.log10((double)countSum)) + 1) - roundedTotalPercent.length();
		System.out.println(bigLine);
		//prints the last row of the table
		System.out.println("TOTAL" + new String(new char[space3]).replace("\0", " ") + countSum + new String(new char[space4]) + roundedTotalPercent + "%");
		//replaces the "-" in bigLine with "=" for the last line
		System.out.println(bigLine.replace("-", "="));
	}
}