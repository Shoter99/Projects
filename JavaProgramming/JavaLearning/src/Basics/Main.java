package Basics;


public class Main extends Read{
	public static void main(String[] args) {
		Read read = new Read();
		read.readFormFile();
		read.separate();
		read.ask();
		read.print("Your points: "+read.points);
	}

}
