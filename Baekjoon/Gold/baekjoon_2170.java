// 선 긋기

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_2170 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<long[]> queue = new PriorityQueue<>(Comparator.comparingLong(arr -> arr[0]));
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long s = Long.parseLong(st.nextToken());
            long e = Long.parseLong(st.nextToken());
            queue.add(new long[] {s, e});
        }

        long[] tmp = queue.poll();
        long s = tmp[0];
        long e = tmp[1];
        long length = e - s;
        while (!queue.isEmpty()) {
            System.out.println(s + " " + e + " " + length);
            long[] next = queue.poll();
            long ns = next[0];
            long ne = next[1];

            if (e <= ns) {
                s = ns;
                e = ne;
                length += (e - s);
            } else if (e <= ne) {
                length += (ne - e);
                e = ne;
            }
        }
        System.out.println(length);
    }
}