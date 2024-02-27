// 골목 대장 호석 - 기능성

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_20168 {
        static int N;
    static int B;
    static int C;
    static int answer = 10001;
    static int[][] graph;
    static void backtracing(int cur, int c, int maxC, boolean[] visited) {
        if (c > C) {
            return;
        }
        if (cur == B) {
            answer = Math.min(answer, maxC);
            return;
        }

        System.out.println(cur + " " + maxC);
        for (int i = 1; i <= N; i++) {
            if (graph[cur][i] == 0 || visited[i]) continue;
            visited[i] = true;
            backtracing(i, c + graph[cur][i], Math.max(maxC, graph[cur][i]), visited);
            visited[i] = false;

        }
        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new int[N+1][N+1];
        int a; int b; int c;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            graph[a][b] = c;
            graph[b][a] = c;
        }

        boolean[] visited = new boolean[N+1];
        backtracing(A, 0, 0, visited);

        if (answer == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }

    }
}
