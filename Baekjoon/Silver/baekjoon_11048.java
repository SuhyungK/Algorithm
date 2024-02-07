// 이동하기 

package Baekjoon.Silver;

import java.io.*;
import java.util.*;

public class baekjoon_11048 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] candyArr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                candyArr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int col = 1; col < M; col++) {
            candyArr[0][col] += candyArr[0][col-1];
        }
        
        for (int row = 1; row < N; row++) {
            candyArr[row][0] += candyArr[row-1][0];
        }

        int[][] dir = new int[][] {{-1, 0}, {0, -1}, {-1, -1}};
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                
                int tmp = Integer.MIN_VALUE;
                for (int d = 0; d < 3; d++) {
                    tmp = Math.max(tmp, candyArr[i + dir[d][0]][j + dir[d][1]]);
                }
                candyArr[i][j] += tmp;
            }
        }

        System.out.println(candyArr[N-1][M-1]);
    }
}