// 문제집

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class baekjoon_1766 {
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int A;
        int B;
        List<List<Integer>> workbook = new ArrayList<>();
        int[] priority = new int[N+1];
        for (int i = 0; i <= N; i++) {
            workbook.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            priority[B]++;
            workbook.get(A).add(B);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i <= N; i++) {
            if (priority[i] == 0) {
                pq.add(i);
            }
        }

        while (!pq.isEmpty()) {
            int problem = pq.poll();
            
            System.out.print(problem + " ");
            for (int nextProblem : workbook.get(problem)) {
                priority[nextProblem]--;
                if (priority[nextProblem] == 0) {
                    pq.add(nextProblem);
                }
            }
        }
        // System.out.println(sb);
        System.out.println();
    }
}
