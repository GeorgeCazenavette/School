/* **************************************************************
 * Jean Gourd
 * GameOfLife.java
 * 2016-09-02
 *
 * Game of Life implementation using a multi-dimensional array.
 ************************************************************** */

//import java.io.*;
import java.util.Scanner;

public class GameOfLife
{
	public static final int MAX_WIDTH = 40;

	private static int numGens = 10;
	private static int genInt = 1;
	private static int animate = 0;
	private static boolean debug = false;

	public static void main(String[] args)
	{
		boolean[][] board;
		ParseCmdLine(args);
		board = ReadGen0();
		if(animate > 0);
			System.out.print("\u001b[2J\u001[H");
		DisplayBoard(board, 0);
		
		
		for (int i = 1; i <= numGens; i++)
		{
			board = ComputeGen(board);
			if (i % genInt == 0)
			{
				Thread.sleep(animate);
				System.out.print("\u001b[2J\u001[H");
				DisplayBoard(board, i);
			}
				
		}
	}

	// parses the command line for parameters
	public static void ParseCmdLine(String[] args)
	{
		if (args.length == 0)
		{
			ShowUsage();
			System.exit(0);
		}

		for (int i=0; i<args.length; i++)
		{
			// default values
			if (args[i].equals("-D"))
				break;
			// help/usage
			if (args[i].equals("-h"))
			{
				ShowUsage();
				System.exit(0);
			}
			// debug
			if (args[i].equals("-d"))
				debug = true;
			// number of generations to produce
			else if (args[i].startsWith("-n"))
				numGens = Integer.parseInt(args[i].substring(2));
			// display generation interval
			else if (args[i].startsWith("-i"))
				genInt = Integer.parseInt(args[i].substring(2));
			// animation delay
			else if (args[i].startsWith("-a"))
				animate = Integer.parseInt(args[i].substring(2));
		}
		// display debug information if specified
		if (debug)
			System.out.println("numGens=" + numGens + "; genInt=" + genInt + "; animate=" + animate);
	}

	// displays help/usage
	public static void ShowUsage()
	{
		System.out.println("Usage: java GameOfLife [-h] -D [-(nia)<val>]");
		System.out.println(" e.g.: java GameOfLife -D < gen0");
		System.out.println("  -D\t\tUse default values");
		System.out.println("  -n<val>\tSet the number of generations to produce to <val> (=10)");
		System.out.println("  -i<val>\tSet the generation display interval to <val> (=1)");
		System.out.println("  -a<val>\tSuperpose each generation and delay <val> milliseconds");
		System.out.println("  -h\t\tShow this screen");
	}

	// reads the initial generation
	public static boolean[][] ReadGen0()
	{
		boolean[][] board = null;
		
		Scanner s = new Scanner(System.in);
		String line;
		int r = 0;
		
		while(s.hasNextLine())
		{
			line = s.nextLine();
			if(r == 0)
			{
				board = new boolean[line.length()][line.length()];
			}
			for(int i = 0; i < line.length(); i++)
			{
				board[r][i] = (line.charAt(i) == '*');
			}
			r++;
		}
		return board;
	}

	// displays the current board
	public static void DisplayBoard(boolean[][] board, int gen)
	{
		System.out.println("Gen" + gen + ":");
		
		for(int r = 1; r < board.length - 1; r++)
		{
			if(r == 1)
			{
				System.out.print("  ");
				for(int c = 1; c < board.length - 1; c++)
					System.out.print(c % 10 + " ");
				System.out.println();
			}
			
			for(int c = 1; c < board.length - 1; c++)
			{
				if(c == 1)
				{
					System.out.print(c % 10 + " " );
				}
				if(board[r][c])
					System.out.print("* ");
				else
					System.out.print("  ");
			}
			System.out.println();
		}
	}

	// given a current generation, computes the next
	public static boolean[][] ComputeGen(boolean[][] board)
	{
		boolean[][] newBoard = new boolean[board.length][board.length];
		
		for(int r = 1; r < board.length - 1; r++)
		{
			for(int c = 1; c < board.length - 1; c++)
			{
				int neighbors = 0;
				for(int i = r - 1; i <= r + 1; i++)
				{
					for(int j = c - 1; j <= c + 1; j++)
					{
						if((i != r || j != c) && board[i][j])
							neighbors++;
					}
				}
				
				if (board[r][c])
				{
					if(neighbors == 2 || neighbors || 3)
						newBoard[r][c] == true;		
				}
				else
					if(neighbors == 3)
						newBoard[r][c] == true;
			}
		}
		
		return newBoard;
	}
}