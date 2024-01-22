package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Stack<Long> stack = new Stack<>();
        stack.add(Long.MAX_VALUE);
        long[] answer = new long[N];
        for (int i = N-1; i >= 0; i--){
            while (arr[i] >= stack.peek()) {
                stack.pop();
            }
            answer[i] = stack.peek();
            stack.add(arr[i]);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            if (answer[i] == Long.MAX_VALUE) {
                answer[i] = -1;
            }
            sb.append(answer[i] + " ");
        }
        System.out.println(sb);
    }
}
