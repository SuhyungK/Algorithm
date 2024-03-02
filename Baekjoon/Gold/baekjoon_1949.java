// 우수 마을

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_1949 {
        static List<List<Integer>> tree;
    static int[] population;
    static int[][] dp;
    static void dfs(int cur, boolean[] visited) {
        dp[cur][0] += population[cur];
        
        visited[cur] = true;
        for (int child : tree.get(cur)) {
            if (visited[child] == true) continue;
            dfs(child, visited);
            dp[cur][0] += dp[child][1];
            dp[cur][1] += Math.max(dp[child][0], dp[child][1]);
        }
        visited[cur] = false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        population = new int[N];
        for (int i = 0; i < N; i++) {
            population[i] = Integer.parseInt(st.nextToken());
        }

        tree = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            tree.add(new ArrayList<>());
        }

        int a; 
        int b;
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            tree.get(a-1).add(b-1);
            tree.get(b-1).add(a-1);
        }

        dp = new int[N][2];
        boolean[] visited = new boolean[N];
        dfs(0, visited);
        
        for (int i = 0; i < dp.length; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }
        System.out.println(Math.max(dp[0][0], dp[0][1]));
    }
}
