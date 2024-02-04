// 동전

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_9084 {
    static void printarr(long[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            int[] coins = new int[N+1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                coins[j+1] = Integer.parseInt(st.nextToken());
            }

            int M = Integer.parseInt(br.readLine());
            long[][] dp = new long[N+1][M+1];
            
            for (int j = 1; j <= N; j++) {
                dp[j][0] = 1;
            }

            for (int j = 1; j <= N; j++) {
                int coin = coins[j];

                for (int k = coin; k <= M; k++) {
                    dp[j][k] += (dp[j-1][k] + dp[j][k-coin]);
                }
            }
            long answer = 0;
            for (int j = 0; j <= N; j++) {
                answer = Math.max(answer, dp[j][M]);
            }
            System.out.println(answer);
        }
    }
}
