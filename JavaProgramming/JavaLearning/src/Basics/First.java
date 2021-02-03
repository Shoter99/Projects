package Basics;

import java.util.Scanner;

public class First {
	
	
	
	static void welcome(String fname) {
		System.out.println("Hello "+ fname+"!");
	}
	static void print(String content) {
		System.out.println(content);
	}
	static String form(int number) {
		if(number == 0 || number == 1) {
			return "candy";
		}
		else return "candies";
	}
	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		print("How many candies do you have: ");
		int numberOfCandies = input.nextInt();
		print("How many students are in your class: ");
		int numberOfStudents = input.nextInt();
		
		int candiesLeft = numberOfCandies%numberOfStudents;
		
		int howManySweets = (numberOfCandies-candiesLeft)/numberOfStudents;
		print("Every student will get "+howManySweets+" "+form(howManySweets));
		print("Candies left: "+candiesLeft);
		input.close();
	}

}
