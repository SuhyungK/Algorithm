// 보석 도둑

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_1202 {
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        long[][] jewelry = new long[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            jewelry[i][0] = Long.parseLong(st.nextToken());
            jewelry[i][1] = -Long.parseLong(st.nextToken());
        }

        long[] bags = new long[K];
        for (int i = 0; i < K; i++) {
            bags[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(jewelry, (a, b) -> (int) (a[0] - b[0]));
        Arrays.sort(bags);

        long answer = 0;
        int idx = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(arr -> arr[1]));
        for (int i = 0; i < K; i++) {
            long bagWeight = bags[i];
            while (idx < N && bagWeight >= jewelry[idx][0]) {
                pq.add(jewelry[idx]);
                idx++;
            }

            if (!pq.isEmpty()) {
                answer -= pq.poll()[1];
            }
        }
        System.out.println(answer);
    }
}
