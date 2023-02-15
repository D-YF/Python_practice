import javax.swing.plaf.synth.SynthEditorPaneUI;

public class Puppy {
    public static void main(String[] args){
        String a = new String("abc");
        // String a = "abc";
        int b, c, d;
        b = c = d = 5;
        a = "abc";
        char me = 'a';

        float decimal = 1.9f;
        double decimal_double = 1.9d;
        int b_int = (int) b;
        boolean myBool = true;
        // b %= 2;
        // b <<= 2;
        // b ++;
        // if (b==b_int && b_int==b)
            // System.out.println( decimal_double == decimal);
        // System.out.println(a + b + me + decimal + decimal_double + myBool + b_int);

        String string = "text's long enough";
        System.out.println(string.length());
        System.out.println(string.toUpperCase());
        System.out.println(string.indexOf("ou"));
        System.out.println(Math.pow(decimal_double, Math.random()*10));

        if (b == c){
            System.out.println("if");
        } else {
            System.out.println("else");
        }
        boolean is_b_equal_decimal = (b==decimal) ? true : false;
        System.out.println(is_b_equal_decimal);

        String[] cars = {"Volvo", "BMW", "Jeep", "Ford", "Mazda"};
        for (String str : cars){
            System.out.println(str);
        }

        int[] array = {1, 2, 3, 4};
        for (int num : array){
            System.out.println(num);
        }
        

    }
}