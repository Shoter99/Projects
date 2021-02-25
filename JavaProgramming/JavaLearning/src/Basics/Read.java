package Basics;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Read{
List<String> data = new ArrayList<String>();
List<String> questions = new ArrayList<String>();
List<String> answers = new ArrayList<String>();
public int points=0;
public void print(String content) {
	System.out.println(content);
}
    public void readFormFile(){
        try{
            File myFile = new File("/home/dawid/questions.txt");
            Scanner myReader = new Scanner(myFile);
            while(myReader.hasNextLine()){
            	data.add(myReader.nextLine());
            }
            myReader.close();
        }catch(FileNotFoundException e){
            System.out.println("No file found");
            e.printStackTrace();
        }
        

    }
    //will separate questions from answers
    public void separate(){
    	int i=1;
        for(String x : data) {
        	if(i%6 == 0) {
        		answers.add(x);
        	}else {
        		questions.add(x);
        	}
        	i++;
        }

    }
    public void ask() {
    	int i =1;
    	int num=0;
    	for(String ans : answers) {
    		print("Now you will get "+i+" question. Get ready!");
    		for(int j=0+num; j<=4+num;j++) {
    			print(questions.get(j));
    		}
    		Scanner output = new Scanner(System.in);
    		print("What is your answer? ");
    		String answer = output.nextLine();
    		
    		if(ans.contentEquals(answer.toUpperCase())) {
    			print("Good job your answer was correct!");
    			points++;
    		}else {
    			print("Your answer was not correct!");
    		}
    		num+=5;
    	}
    }
    

}