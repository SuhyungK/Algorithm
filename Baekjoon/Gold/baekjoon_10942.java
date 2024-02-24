// 팰린드롬?

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_10942 {
        static int[] numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        numbers = new int[N+1];
        numbers[0] = -1;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N+1][N+1];
        for (int j = 1; j <= N; j++) {
            dp[j][j] = 1;
            if (numbers[j] == numbers[j-1]) {
                dp[j-1][j] = 1;
            }

            for (int i = 1; i < j - 1; i++) {
                if (numbers[i] == numbers[j] && dp[i+1][j-1] == 1) {
                    dp[i][j] = 1;
                }
            }
        }

        int M = Integer.parseInt(br.readLine());
        int S; int E;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            sb.append(dp[S][E] + "\n");
        }
        System.out.println(sb);
    }
}
