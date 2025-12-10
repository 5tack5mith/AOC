import java.util.*;
import java.io.FileNotFoundException;
import java.io.*;
public class Part2{
    public static void main(String[] args) throws Exception{
        int count =0;
        int z =0;
        try{
            File file = new File("input.txt");
            Scanner sc = new Scanner(file);
            int pos = 50;
            while(sc.hasNextLine()){
                String line = sc.nextLine();
                char lr = line.charAt(0);
                int r = Integer.parseInt(line.substring(1));
                if(lr=='R'){
                    z+=r/100;
                    r=r%100;
                    if((r+pos)<=100){}
                    else{
                        z++;
                    }
                    pos = (pos+r)%100;
                }
                else{
                    z+=r/100;
                    r=r%100;
                    if(pos<r){
                        if(pos!=0)z++;
                        pos=100-(r-pos);
                    }
                    else{
                        //if(pos==r && pos!=0){z++;}
                        pos=pos-r;
                    }
                }
                if(pos==0 && r!=0){
                    count++;
                    z++;
                }
            }
            sc.close();
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
        System.out.println(z);
    }
}


