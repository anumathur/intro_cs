
public class CreditCard {

	String cc; 
	boolean valid; 
	int errorCode;
	
	//constructor setting values
	public CreditCard (String CreditCard)
	
	{
		cc = CreditCard;
		valid = true; 
		errorCode = 0;
	} 
	
	public void check()
	{
		// converts each number in the cc String to an int
		int first = Integer.parseInt(Character.toString(cc.charAt(0))); 
		int second = Integer.parseInt(Character.toString(cc.charAt(1))); 
		int third =  Integer.parseInt(Character.toString(cc.charAt(2)));
		int fourth = Integer.parseInt(Character.toString(cc.charAt(3))); 
		int fifth = Integer.parseInt(Character.toString(cc.charAt(4)));
		int sixth = Integer.parseInt(Character.toString(cc.charAt(5)));
		int seventh = Integer.parseInt(Character.toString(cc.charAt(6)));
		int eighth = Integer.parseInt(Character.toString(cc.charAt(7)));
		int ninth = Integer.parseInt(Character.toString(cc.charAt(8)));
		int tenth = Integer.parseInt(Character.toString(cc.charAt(9)));
		int eleventh = Integer.parseInt(Character.toString(cc.charAt(10)));
		int twelfth = Integer.parseInt(Character.toString(cc.charAt(11)));
		
		// sum needed for one of the checks
		int sum = 0;
		for (int i = 0; i < 12; i++) 
		{
			sum = sum + Integer.parseInt(Character.toString(cc.charAt(i)));
		}
		
		//credit card validity checks
		if (first != 4)
		{
			valid = false;
			errorCode = 1;
		}
		
		else if (fourth != fifth + 1)
		{
			valid = false;
			errorCode = 2; 
		}
		
		else if (first*fifth*ninth != 24)
		{
			valid = false;
			errorCode = 3;
		}
		
		else if (sum % 4 != 0)
		{
			valid = false;
			errorCode = 4;
		}
		
		
		else if (first + second + third + fourth + 1 != ninth + tenth + eleventh 
				+ twelfth)
		{
			valid = false; 
			errorCode = 5; 
		}
		
		else if (first*10 + second + seventh*10 + eighth != 100)
		{
			valid = false; 
			errorCode = 6;
		}
		
		//if none are true, then it is false
		else 
		{
			valid = true; 
		}
		
		
	}
		
	// returns whether the credit card number is valid or not
	public boolean isValid()
	{
		return valid;
	}
	
	// returns which criteria makes the error code wrong
	// value will be 0 if there is no error
	public int getErrorCode()
	{
		return errorCode;
	}
}
