// 곡예 비행

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_21923 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] upLeft = new int[N][M];
        upLeft[N-1][0] = arr[N-1][0];
        for (int i = 1; i < M; i++) {
            upLeft[N-1][i] += upLeft[N-1][i-1] + arr[N-1][i];
        }   

        for (int i = N-2; i > -1; i--) {
            upLeft[i][0] += upLeft[i+1][0] + arr[i][0];
        }

        for (int i = N-2; i > -1; i--) {
            for (int j = 1; j < M; j++) {
                upLeft[i][j] = Math.max(upLeft[i+1][j], upLeft[i][j-1]) + arr[i][j];
            }
        }

        int[][] rightDown = new int[N][M];
        rightDown[N-1][M-1] = arr[N-1][M-1];
        for (int j = M-2; j > -1; j--) {
            rightDown[N-1][j] += rightDown[N-1][j+1] + arr[N-1][j];
        }

        for (int i = N-2; i > -1; i--) {
            rightDown[i][M-1] += rightDown[i+1][M-1] + arr[i][M-1];
        }

        for (int i = N-2; i > -1; i--) {
            for (int j = M-2; j > -1; j--) {
                rightDown[i][j] = Math.max(rightDown[i+1][j], rightDown[i][j+1]) + arr[i][j];
            }
        }
        
        long answer = Long.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                answer = Math.max(answer, upLeft[i][j] + rightDown[i][j]);
            }
        }

        System.out.println(answer);
    }
}