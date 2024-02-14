// 과제 

package Baekjoon.Gold;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class baekjoon_13904 {
        public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[][] assignment = new int[N][2];
        for (int i = 0; i < N; i++) {
            assignment[i][0] = sc.nextInt();
            assignment[i][1] = sc.nextInt();
        }

        Arrays.sort(assignment, (a, b) -> {
            if (a[0] != b[0]) return b[0] - a[0];
            return b[1] - a[1];
        });

        int finalDay = assignment[0][0];
        int idx = 0;
        int maxScore = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        while (finalDay > 0 && idx < N) {

            while (idx < N && finalDay == assignment[idx][0]) {
                queue.add(-assignment[idx][1]);
                idx++;
            }
            System.out.println(queue);

            if (!queue.isEmpty()) {
                maxScore -= queue.poll();
            }
            finalDay--;
        }
        System.out.println(maxScore);
    }
}
