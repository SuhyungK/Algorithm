package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_2533 {
    static List<List<Integer>> arr;
    static int[][] dp;
    static boolean[] visited;
    
    public static void dfs(int parent) {
        dp[parent][0] = 1;
        visited[parent] = true;
        System.out.println("parent : " + parent);
        for (int child: arr.get(parent)) {
            if (visited[child]) continue;
            dfs(child);
            
            dp[parent][0] += Math.min(dp[child][0], dp[child][1]);
            dp[parent][1] += dp[child][0];
            // System.out.println(parent + ", " + child + " : " + Arrays.toString(dp[parent]));
        }

        System.out.println(parent + " : " + Arrays.toString(dp[parent]));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new ArrayList<>(N+1);
        dp = new int[N+1][2];
        visited = new boolean[N+1];
        
        for (int i = 0; i <= N; i++) {
            arr.add(new ArrayList<>());
        }

        StringTokenizer st;
        int u; int v;
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            arr.get(u).add(v);
            arr.get(v).add(u);
        }

        dfs(1);
        System.out.println(Math.min(dp[1][0], dp[1][1]));
    }
}
