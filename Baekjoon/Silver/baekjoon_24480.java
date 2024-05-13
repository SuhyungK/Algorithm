// 알고리즘 수업 - 깊이 우선 탐색 2

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_24480 {
    static int N;
    static int M;
    static int R;
    static int[] orders;
    static List<List<Integer>> graph;
    static int orderNum = 1;

    static void dfs(int cur) {
        if (orders[cur] != 0) {
            return;
        }

        orders[cur] = orderNum++;
        for (int next : graph.get(cur)) {
            dfs(next);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        orders = new int[N];
        graph = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        graph.stream().forEach(each -> Collections.sort(each, Collections.reverseOrder()));

        dfs(R-1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < orders.length; i++) {
            sb.append(orders[i] + "\n");
        }
        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb);
    }
}