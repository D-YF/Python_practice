import java.util.*;

public class My_String {

    public static String StackReverse(char[] str){
        Stack<Character> st = new Stack<>();
        for (int i=0; i<str.length; i++){
            st.push(str[i]);
        }
        for (int i=0; i<str.length; i++){
            str[i] = st.pop();
        }
        return String.valueOf(str);
    }

    public static String InterativeReverse(String str){
        char[] charArray = str.toCharArray();
        int left = 0;
        int right = str.length()-1;
        while(left < right){
            char temp = charArray[left];
            charArray[left] = charArray[right];
            charArray[right] = temp;
            left ++;
            right --;
        }
        return String.valueOf(charArray);
    }

    public static String LeftRotate(String str, int step){
        return str.substring(step) + str.substring(0, step);
    }

    public static String HashSortString(String str){
        // Hash table
        int[] letters = new int[26];
        char[] buff = str.toCharArray();
        for (char c: buff){
            letters[c-'a'] ++;
        }
        int k=0;
        for (int i=0; i<26; i++){
            for(int j=0; j<letters[i]; j++){
                buff[k++] = (char) (i + 'a');
            }
        }
        return String.valueOf(buff);
    }

    public static String InsertChar(String str, int[] positions){
        String ans = "";
        int j = 0;
        for(int i=0; i<str.length(); i++){
            if (j<positions.length && i==positions[j] ){
                ans += "*";
                j++;
            }
            ans += str.charAt(i);
        }
        return ans;
    }

    public static void main(String args[]){
        // String function
        String str1 = "Search indexOf a character.";
        int index1 = str1.indexOf("de", 3);
        int index2 = str1.lastIndexOf("a");
        int char1 = str1.charAt(4);
        System.out.println(index1+ " "+ index2 + " " + char1);
        System.out.println(str1.contains("ind"));
        System.out.println(str1.startsWith("Sear"));

        // Stack to reverse
        String str2 = "abcdefg";
        str2 = StackReverse(str2.toCharArray());
        System.out.println(str2);

        // Two pointers to reverse
        String str3 = "abcdefg";
        str3 = InterativeReverse(str3);
        System.out.println(str3);

        // inbuild function
        String str4 = "abcdefg";
        StringBuffer sb = new StringBuffer(str4);
        sb.reverse();
        str4 = sb.toString();
        System.out.println(str4);

        // Left rotate
        String str5 = "leftrotate";
        str5 = LeftRotate(str5, 2);
        System.out.println(str5);

        // Sort using inbuild function
        // O(NlogN)
        String str6 = "adbeacbedcadefb";
        char[] buff = str6.toCharArray();
        Arrays.sort(buff);
        str6 = String.valueOf(buff);
        System.out.println(str6);

        // Sort using hash table
        String str7 = "adbeacbedcadefb";
        str7 = HashSortString(str7);
        System.out.println(str7);

        String str8 = "Insert in certain positions";
        int[] positions = {2,4,5,7};
        str8 = InsertChar(str8, positions);
        System.out.println(str8);



    }
}
