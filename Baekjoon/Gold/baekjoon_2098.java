// 외판원 순회

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_2098 {
        static int N;
    static int[][] cost;
    static long[][] dp;
    static final long INF = Long.MAX_VALUE / 2;
    static long answer = INF;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        cost = new int[N][N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                cost[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        dp = new long[N][1 << N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dp[i], -1);
        }

        System.out.println(dfs(0, 1));
    }

    static long dfs(int cur, int state) {
        if (state == (1 << N) - 1) {
            if (cost[cur][0] == 0) return INF;
            else return cost[cur][0];
        }
        if (dp[cur][state] != -1) return dp[cur][state];
        
        dp[cur][state] = INF;
        for (int i = 0; i < N; i++) {
            if (cost[cur][i] != 0 && (state & (1 << i)) == 0) {
                dp[cur][state] = Math.min(dp[cur][state], dfs(i, state | (1 << i)) + cost[cur][i]);
            }
        }
        return dp[cur][state];
    }

}
