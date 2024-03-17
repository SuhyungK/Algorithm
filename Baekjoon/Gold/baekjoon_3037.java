// 혼란

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_3037 {
    static final int MOD = 1_000_000_007;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();

        long[][] dp = new long[2][C+1];
        dp[0][0] = 1;
        for (int i = 1; i <= N; i++) {
            dp[i%2][0] = 1;
            for (int j = 1; j <= C; j++) {
                dp[i%2][j] = (dp[i%2][j-1] + dp[1-i%2][j] - (j >= i ? dp[1-i%2][j-i] : 0) + MOD) % MOD;
            }
        }   
        System.out.println(dp[N%2][C]);
    }
}