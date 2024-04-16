// 스택 2

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class baekjoon_28278 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int input = Integer.parseInt(st.nextToken());
            if (input == 1) {
                stack.add(Integer.parseInt(st.nextToken()));
            } else if (input == 2) {
                if (!stack.isEmpty()) {
                    sb.append(stack.pop() + "\n");
                } else {
                    sb.append(-1 + "\n");
                }
            } else if (input == 3) {
                sb.append(stack.size() + "\n");
            } else if (input == 4) {
                sb.append((stack.isEmpty() ? 1 : 0) + "\n");
            } else if (input == 5) {
                sb.append((!stack.isEmpty() ? stack.peek() : -1) + "\n");
            }
        }
        sb.deleteCharAt(sb.length()-1);
        System.out.println(sb);
    }
}