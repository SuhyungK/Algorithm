package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class baekjoon_23083 {
    public static int rem = 1_000_000_000 + 7;
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int[][] honeycomb = new int[N][M];
        int K = sc.nextInt();
        int x; int y;
        for (int i = 0; i < K; i++) {
            x = sc.nextInt();
            y = sc.nextInt()
            honeycomb[x-1][y-1] = -1;
        }

        honeycomb[0][0] = 1;
        int nextRow; int nextCol;
        int[][][] dir = new int[][][] {{{-1, 1}, {0, 1}, {1, 0}}, {{0, 1}, {1, 1}, {1, 0}}};
        
        for (int col = 0; col < M; col++) {
            for (int row = 0; row < N; row++) {
                if (honeycomb[row][col] == -1) continue;

                for (int k = 0; k < 3; k++) {
                    nextRow = row + dir[col%2][k][0];
                    nextCol = col + dir[col%2][k][1];

                    if (nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M || honeycomb[nextRow][nextCol] == -1) continue;
                    honeycomb[nextRow][nextCol] += honeycomb[row][col];
                    honeycomb[nextRow][nextCol] %= rem;
                }
            }
        }

        System.out.println(honeycomb[N-1][M-1] % rem);
        
    }
}
