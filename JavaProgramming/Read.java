public class Read(){
String[] data;
    public void readFormFile(){
        try{
            File myFile = new File("questions.txt");
            Scanner myReader = new Scanner(myFile);
            while(myReader.hasNextLine()){
                data.append(myReader.nextLine());

            }
            myReader.close();
        }catch(FileNotFoundException e){
            System.out.println("No file found");
            e.printStackTrace();
        }
        

    }
    //will separate questions from answers
    public void separate(){
        System.out.println(data);

    }

}