package Baekjoon.Platinum;

import java.io.*;
import java.util.*;

public class baekjoon_3015 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        Stack<long[]> stack = new Stack<>();
        long answer = 0;
        for (int i = 0; i < N; i++) {
            long sameCount = 1L;
            while (!stack.isEmpty()) {
                if (arr[i] <= stack.peek()[0]) {
                    answer++;
                    break;
                }

                if (arr[i] > stack.peek()[0]) {
                    answer += stack.pop()[1];
                    continue;
                } else {
                    answer += stack.peek()[1];
                    sameCount += stack.pop()[1];
                    // an
                }
            }
            stack.add(new long[] {arr[i], sameCount});
        }
        System.out.println(answer);
    }
}
