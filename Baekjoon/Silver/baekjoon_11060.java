// 점프 점프

package Baekjoon.Silver;

import java.util.*;
import java.io.*;

public class baekjoon_11060 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] miro = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            miro[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[N];
        Arrays.fill(dp, 1001);
        dp[0] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j <= Math.min(i + miro[i], N-1); j++) {
                if (dp[j] > dp[i] + 1) {
                    dp[j] = dp[i] + 1; 
                }
            }
        }

        System.out.println(dp[N-1] == 1001 ? -1 : dp[N-1]);
    }
}