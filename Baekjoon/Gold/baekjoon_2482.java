// 색상환

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_2482 {
    static int MOD = 1_000_000_003;

    static int sol(int N, int K) {

        if (N / 2 < K) {
            return 0;
        }

        int[][] dp = new int[N + 1][K + 1];

        for (int i = 1; i <= N; i++) {
            dp[i][1] = i;
        }

        for (int i = 4; i <= N; i++) {
            for (int j = 2; j <= K; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % MOD;
            }
        }

        System.out.println();
        for (int i = 0; i < dp.length; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }
        System.out.println();
        return dp[N][K];
    }
    
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        System.out.println(sol(N, K));
    }
}