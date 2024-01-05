package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_6198 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[] buildings = new long[N+1];
        for (int i = 0; i < N; i++) {
            buildings[i] = Long.parseLong(br.readLine());
        }
        buildings[N] = Long.MAX_VALUE;

        Stack<Integer> st = new Stack<>();
        long[] count = new long[N];
        for (int i = 0; i < N + 1; i++) {
            while (!st.isEmpty() && buildings[st.peek()] <= buildings[i]) {
                /**
                 * 스택의 가장 위에 있는 값보다 현재 비교하려는 빌딩 높이가 더 높다면 제거 해야 함
                 */
                count[st.peek()] = i - st.peek() - 1L;
                st.pop();
            }
            st.add(i);
        }

        System.out.println(Arrays.stream(count).sum());
    }
}
