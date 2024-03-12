// 암호코드

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_2011 {
    static final int DIVIDE = 1000000;
    static int check1(int a) {
        return 0 < a && a < 10 ? 1 : 0;
    }

    static int check2(int a, int b) {
        int tmp = 10 * a + b;
        return a != 0 && 1 <= tmp && tmp <= 26 ? 1 : 0;
    }

    static int solution(int n, int[] dp, int[] arr) {
        if (arr[0] == 0) return 0;
        if (n > 1) {
            dp[1] = check1(arr[1]) + check2(arr[0], arr[1]);
            
            for (int i = 2; i < n; i++) {
                dp[i] = dp[i-2] * check2(arr[i-1], arr[i]) + dp[i-1] * check1(arr[i]);
                dp[i] %= DIVIDE;
            }
        }

        System.out.println(Arrays.toString(dp));
        return dp[n-1];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("");
        int[] arr = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }
        
        int[] dp = new int[input.length];
        dp[0] = 1;
        System.out.println(solution(arr.length, dp, arr));
    }
}