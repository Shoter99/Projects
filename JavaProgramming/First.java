
public class First {
	static void welcome(String fname) {
		System.out.println("Hello "+ fname+"!");
	}
	
	
	
	public static void main(String[] args) {
		
		if(args.length != 0) {
			String name = args[0];
			welcome(name);
		}else
		welcome("Dawid");
		

	}

}
