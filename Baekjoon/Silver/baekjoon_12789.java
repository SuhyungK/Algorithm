// 도키도키 간식드리미

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class baekjoon_12789 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> tmp = new Stack<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            tmp.add(Integer.parseInt(st.nextToken()));
        }
        Stack<Integer> s1 = new Stack<>();
        while (!tmp.isEmpty()) {
            s1.add(tmp.pop());
        }

        Stack<Integer> s2 = new Stack<>();
        int cur = 1;
        String answer = "Nice";
        while (cur <= N) {
//            System.out.println("s1 = " + s1);
//            System.out.println("s2 = " + s2);
//            System.out.println();
            if (!s2.isEmpty() && s2.peek() == cur) {
                s2.pop();
                cur++;
                continue;
            }

            while (!s1.isEmpty() && s1.peek() != cur) {
                s2.add(s1.pop());
            }

            if (s1.isEmpty()) {
                answer = "Sad";
                break;
            }

            cur++;
            s1.pop();
        }

        System.out.println(answer);
    }
}