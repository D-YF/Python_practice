import java.util.Scanner;

import javax.imageio.stream.ImageOutputStream;

import java.time.*;
import java.util.ArrayList;
import java.util.Collections;


class vehicle{
    String name;
}

public class Main extends vehicle {
    int x;
    enum Size{
        Small,
        Medium,
        Big
    }
    
    public Main(int y){
        x = y;
    }
    
    public static void main(String[] args){
        LocalTime time = LocalTime.now();
        Scanner st = new Scanner(System.in);
        // String username = st.nextLine();

        Main myObj = new Main(99);
        
        int s = sum(5);
        System.out.println(s);
        // myObj.x = 20;
        System.out.println(myObj.x);
        for (Size size : Size.values()){
            System.out.println(size);
        }

        System.out.println(time);

        st.close();

        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Toyata");
        cars.add("Mini");
        cars.add("BMW");
        Collections.sort(cars);
        iterate(cars);

        String my_str = "I think I need more practice!";
        String reverse = "";
        String[] split = my_str.split(" ", 7);
        for (String word: split)
            System.out.println(word);

        for (int i=0; i<my_str.length(); i++){
            reverse = my_str.charAt(i) + reverse;
        }
        System.out.println(reverse);

    }

    static int sum(int n){
        if (n==0) return 0;
        else return n+sum(n-1);
    }


    static void iterate(ArrayList<String> cars){
        System.out.println(cars.size());

        for (String str: cars){
            System.out.println(str);
        }
    }

}