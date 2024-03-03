// 대기업 승범이네 

package Baekjoon.Platinum;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_17831 {
        static List<List<Integer>> tree = new ArrayList<>();
    static int[] talent;
    static void dfs(int cur, long[][] dp) {
        if (tree.get(cur).size() == 0) {
            return;
        }

        int totalSum = 0;
        for (int child : tree.get(cur)) {
            dfs(child, dp);
            totalSum += Math.max(dp[child][0], dp[child][1]);
        }
        dp[cur][1] += totalSum;

        for (int selectChild : tree.get(cur)) {
            if (dp[selectChild][0] > dp[selectChild][1]) {
                dp[cur][0] = Math.max(dp[cur][0], (totalSum - dp[selectChild][0]) + dp[selectChild][1] + talent[selectChild] * talent[cur]);
            } else {
                dp[cur][0] = Math.max(dp[cur][0], totalSum + talent[selectChild] * talent[cur]);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            tree.add(new ArrayList<>());
        }
        
        int par;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N; i++) {
            par = Integer.parseInt(st.nextToken());
            tree.get(par-1).add(i);
        }

        talent = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            talent[i] = Integer.parseInt(st.nextToken());
        }
        
        long[][] dp = new long[N][2];
        dfs(0, dp);
        // for (int i = 0; i < dp.length; i++) {
        //     System.out.println(Arrays.toString(dp[i]));
        // }

        System.out.println(Math.max(dp[0][0], dp[0][1]));
    }
}
