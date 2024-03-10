// 가운데를 말해요

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_1665 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int[] arr;
        arr = new int[M];
        for (int i = 0; i < M; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Queue<Integer> queue1 = new PriorityQueue<>();
        Queue<Integer> queue2 = new PriorityQueue<>();
        queue1.add(-arr[0]);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < M; i++) {
            sb.append(-queue1.peek() + "\n");

            if (-queue1.peek() <= arr[i]) {
                queue2.add(arr[i]);
            } else {
                queue1.add(-arr[i]);
            }

            while (queue1.size() < queue2.size()) {
                queue1.add(-queue2.poll());
            }

            while (queue1.size() > queue2.size() + 1) {
                queue2.add(-queue1.poll());
            }
        }
        sb.append(-queue1.peek() + "\n");
        System.out.println(sb);
    }
}