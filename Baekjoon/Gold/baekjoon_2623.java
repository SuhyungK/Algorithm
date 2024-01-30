// 음악프로그램

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_2623 {
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int[] predecessor = new int[N+1];
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(st.nextToken());
            int X = Integer.parseInt(st.nextToken());
            for (int j = 0; j < K-1; j++) {
                int Y = Integer.parseInt(st.nextToken());
                graph.get(X).add(Y);
                predecessor[Y]++;
                X = Y;
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (predecessor[i] == 0) queue.add(i);
        }

        List<Integer> answer = new ArrayList<>();
        while (!queue.isEmpty()) {
            int q = queue.poll();
            
            answer.add(q);
            for (int next : graph.get(q)) {
                predecessor[next]--;
                if (predecessor[next] == 0) queue.add(next);
            }
        }

        if (answer.size() < N) {
            System.out.println(0);
        } else {
            answer.forEach(i -> System.out.println(i));
        }
    }
}
