import java.util.Random; 


public class Drunkard {

	// instance variables for both original, and current X and Y values
	int currentX; 
	int currentY; 
	int originalX; 
	int originalY; 
	
	/* constructor setting the initial and current X and Y values to the values
	entered by the user */
	public Drunkard (int x, int y)
	{ 
		currentX = x; 
		originalX = x; 
		currentY = y; 
		originalY = y; 
	}
	
	// moves the user randomly one step in any direction (N, S, E, W)
	public void step()
	{
		Random rand = new Random(); 
		int r = rand.nextInt(4);
		
		if (r==0)
			currentX++; // east
		else if (r==1)
			currentX--; // west
		else if (r==2) 
			currentY++; // north
		else if (r==3)
			currentY--; // south
	}
	
	//loops through step a certain number of times
	public void fastForward(int steps) 
	{
		for (int i = 0; i <= steps; i++)
		{
			this.step(); 
		}
		
	}
	
	/*finds the Manhattan distance between the current and original 
	intersections */
	public int howFar()
	{
		int distance = Math.abs(originalX-currentX) + Math.abs(originalY-
				currentY); 
		return distance;
	}
	
	//returns the current location
	public String getLocation()
	{ 
		String s = currentX + "avenue" + currentY + "street"; 
		return s; 
	}
}
