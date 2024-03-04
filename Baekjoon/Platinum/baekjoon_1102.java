// 발전소

package Baekjoon.Platinum;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_1102 {
    static int N;
    static int P;
    static int[][] power;
    static int[] dp;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        power = new int[N][N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                power[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        String powerState = br.readLine();
        P = Integer.parseInt(br.readLine());

        int curVar = 0;
        int initCnt = 0;
        for (int i = 0; i < N; i++) {
            if (powerState.charAt(i) == 'Y') {
                curVar |= (1 << i);
                initCnt++;
            }
        }

        dp = new int[1<<N];
        Arrays.fill(dp, INF);
        if (initCnt >= P) dp[curVar] = 0;
        dfs(curVar, initCnt);
        System.out.println(dp[curVar] == INF ? -1 : dp[curVar]);
    }

    static int dfs(int cur, int cnt) {
        if (cnt >= P) return 0;
        if (dp[cur] != INF) return dp[cur];
        
        for (int i = 0; i < N; i++) {
            if ((cur & (1 << i)) != 0) continue; // 이미 켜진 발전소라면 지나감

            for (int j = 0; j < N; j++) {
                if ((cur & (1 << j)) == 0) continue; // 꺼진 발전소로는 다른 꺼진 발전소를 킬 수 없으므로 지나감
                
                dp[cur] = Math.min(dp[cur], dfs(cur | (1 << i), cnt + 1) + power[j][i]);
            }
        }
        return dp[cur];
    }
}
