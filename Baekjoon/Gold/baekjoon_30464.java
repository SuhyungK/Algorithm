// 시간낭비

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_30464 {
    static int[] pos;
    static int N;
    static int[][] dp;
    
    public static int f(int cur, int u) {
        if (cur < 0 || cur >= N) return Integer.MIN_VALUE;
        if (cur == N-1) return 0;
        if (dp[cur][u] != -1) return dp[cur][u];
        
        dp[cur][u] = Integer.MIN_VALUE;
        if (u == 0) {
            dp[cur][u] = Math.max(f(cur + pos[cur], u), f(cur - pos[cur], u+1)) + 1;
        } else if (u == 1) {
            dp[cur][u] = Math.max(f(cur - pos[cur], u), f(cur + pos[cur], u+1)) + 1;
        } else {
            dp[cur][u] = f(cur + pos[cur], u) + 1;
        }

        return dp[cur][u];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        pos = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            pos[i] = Integer.parseInt(st.nextToken());
        }
        
        dp = new int[N][3];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dp[i], -1);
        }

        // dp[0][0] = 0;
        int answer = f(0, 0);
        System.out.println(answer > 0 ? answer : -1);
    }
}