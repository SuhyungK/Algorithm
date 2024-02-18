// 주지수

package Baekjoon.Silver;

import java.util.*;
import java.io.*;

public class baekjoon_15724 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        long[][] square = new long[N+1][M+1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= M; j++) {
                square[i][j] = Long.parseLong(st.nextToken());
            }
        }
        
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                square[i][j] += square[i][j-1];
            }
        }

        for (int j = 1; j <= M; j++) {
            for (int i = 1; i <= N; i++) {
                square[i][j] += square[i-1][j];
            }
        }

        System.out.println();
        for (int i = 0; i < square.length; i++) {
            System.out.println(Arrays.toString(square[i]));
        }
        System.out.println();

        int x1;
        int y1;
        int x2; 
        int y2;
        int K = Integer.parseInt(br.readLine());
        long[] answer = new long[K];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            answer[i] = square[x2][y2] - square[x1-1][y2] - square[x2][y1-1] + square[x1-1][y1-1];
            System.out.println(square[x2][y2] + " " + square[x1-1][y2] + " " + square[x2][y1-1] + " " + square[x1-1][y1-1]);
        }

        for (int i = 0; i < K; i++) {
            System.out.println(answer[i]);
        }
    }
}