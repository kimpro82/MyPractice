class NumThread extends Thread
{
	public void run()
	{
		for (int i = 0; i <= 26; i++)
		{
			System.out.print(i);
			try
			{
				Thread.sleep(250);				
			}
			catch (Exception e) {}
		}
	}
}

class CharThread extends Thread
{
	public void run()
	{
		for (char letter = 'A'; letter <='Z' ; letter++)
		{
			System.out.print(letter);
			try
			{
				Thread.sleep(250);				
			}
			catch (Exception e) {}
		}
	}
}

public class MultiThread
{
	public static void main(String args[])
	{
		Thread thread1 = new NumThread();
		Thread thread2 = new CharThread();
		thread1.start();
		thread2.start();
	}
}