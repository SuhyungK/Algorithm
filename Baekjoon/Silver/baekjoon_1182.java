// 부분 수열의 합

package Baekjoon.Silver;

import java.io.*;
import java.util.StringTokenizer;

public class baekjoon_1182 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] sequence = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for (int i = 1; i < Math.pow(2, N); i++) {
            int tmpSum = 0;
            for (int j = 0; j < N; j++) {
                if ((i & (1 << j)) != 0) {
                    // System.out.println((i & (1 << j)));
                    tmpSum += sequence[j];
                }
            }

            // System.out.println(i + " " + tmpSum);
            if (tmpSum == S) {
                answer++;
            }
        }
        System.out.println(answer);
    }
}
