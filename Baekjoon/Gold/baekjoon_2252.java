// 줄 세우기

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_2252 {
        public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] inDegree = new int[N]; // 진입 차수
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        int A;
        int B;
        for (int i = 0; i < M; i++) {
            A = sc.nextInt();
            B = sc.nextInt();
            inDegree[B-1]++;
            graph.get(A-1).add(B-1);
        }

        Queue<Integer> queue = findStart(inDegree);

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            int node = queue.poll();
            sb.append(node+1)
              .append(" ");

            List<Integer> linkedNode = graph.get(node);
            for (Integer i : linkedNode) {
                inDegree[i]--;
                if (inDegree[i] == 0) {
                    queue.add(i);
                }
            }
        }

        System.out.println(sb);
    }

    private static Queue<Integer> findStart(int[] inDegree) {
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < inDegree.length; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }
        return queue;
    }
}
