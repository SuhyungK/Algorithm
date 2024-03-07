// 중앙값 구하기

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_2696 {
    static final int LIMIT_NUMBER = 10;
    
    static int[] solution(int M, int[] arr) {
        Queue<Integer> lowQ = new PriorityQueue<>();
        Queue<Integer> highQ = new PriorityQueue<>();
        highQ.add(arr[0]);
        
        int[] answer = new int[(M+1)/2];
        answer[0] = arr[0];
        for (int i = 1; i < M; i++) {
            if (arr[i] >= highQ.peek()) {
                highQ.add(arr[i]);
            } else {
                lowQ.add(-arr[i]);
            }

            if (i % 2 == 1) continue; // 짝수면 지나감

            while (highQ.size() != (lowQ.size() + 1)) {
                if (highQ.size() > lowQ.size()) {
                    lowQ.add(-highQ.poll());
                } else {
                    highQ.add(-lowQ.poll());
                }
            }

            answer[i/2] = highQ.peek();
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        int M;
        int[] arr;
        StringTokenizer st;
        while (T-- > 0) {
            M = Integer.parseInt(br.readLine());
            arr = new int[M];
            int row = 0;
            while (M > 0) {
                st = new StringTokenizer(br.readLine());
                for (int col = 0; col < Math.min(M, 10); col++) {
                    arr[10 * row + col] = Integer.parseInt(st.nextToken());
                }
                M -= 10;
                row++;
            }

            int[] answer = solution(arr.length, arr);
            System.out.println(answer.length);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < answer.length; i++) {
                sb.append(answer[i] + " ");
                if ((i+1) % 10 == 0) sb.append("\n");
            }
            System.out.println(sb);
        }
    }
}