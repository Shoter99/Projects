package Basics;

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Read{
List<String> data = new ArrayList<String>();
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
        

    }

}