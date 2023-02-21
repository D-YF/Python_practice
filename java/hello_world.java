abstract class parent{
    public void print(){
        System.out.println("Hello Parent!");
    }

}

public class hello_world extends parent{
    public static void main(String[] args){
        parent child = new hello_world();
        child.print();
        System.out.println("Hello World!");
    }
}

class Solution {
    public int numSquares(int n) {
            int[] dp = new int[n+1];
            int max = Integer.MAX_VALUE;
            for (int j=1; j<=n; j++){
                dp[j] = max;
            }
            dp[0] = 0;

            // for (int j=0; j<=n; j++){
                // for (int i=0; i*i <= j; i++){
            for (int i=1; i*i<=n; i++){
                for (int j=i*i; j<=n; j++){
                    if (dp[j-i*i] != max) dp[j] = Math.min(dp[j], dp[j-i*i]+1);
                }
            }

            return dp[n];
    }
}

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int j=0; j<=s.length(); j++){
            for (String word : wordDict){
                int len = word.length();
                if (j>=len && dp[j-len] && word.equals(s.substring(j-len,j))){
                    dp[j] = true;
                }
            }
        }
        return dp[s.length()];
    }
}