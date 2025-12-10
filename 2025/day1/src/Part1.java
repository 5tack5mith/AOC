import java.util.*;
import java.io.FileNotFoundException;
import java.io.*;
public class Part1{
    public static void main(String[] args) throws Exception{
        int count =0;
        try{
            File file = new File("input.txt");
            Scanner sc = new Scanner(file);
            int pos = 50;
            while(sc.hasNextLine()){
                String line = sc.nextLine();
                char lr = line.charAt(0);
                int r = Integer.parseInt(line.substring(1));
                if(lr=='R'){
                    pos = (pos+r)%100;
                }
                else{
                    r=r%100;
                    if(pos<r){
                        pos=100-(r-pos);
                    }
                    else{
                        pos=pos-r;
                    }
                }
                if(pos==0){
                    count++;
                }
            }
            sc.close();
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
        System.out.println(count);
    }
}