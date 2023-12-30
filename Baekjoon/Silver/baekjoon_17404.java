// RGB 거리 2

package Baekjoon.Silver;

import java.util.Scanner;

public class baekjoon_17404 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[][] RGB = new int[N][3];
        for (int i = 0; i < RGB.length; i++) {
            for (int j = 0; j < RGB[0].length; j++) {
                RGB[i][j] = sc.nextInt();
            }
        }
        
        int[][][] dp = new int[N][3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == j) dp[1][i][j] = 2002;
                else dp[1][i][j] = RGB[0][j] + RGB[1][i];
            }
        }

        for (int i = 2; i < dp.length; i++) {
            for (int j = 0; j < dp[0].length; j++) {
                for (int k = 0; k < dp[0][0].length; k++) {
                    dp[i][j][k] = Math.min(dp[i-1][(j+1)%3][k], dp[i-1][(j+2)%3][k]) + RGB[i][j];
                    System.out.println(i + " " + j + " " + k);
                    System.out.println(i + " " + (j+1)%3 + " " + k);
                    System.out.println(i + " " + (j+2)%3 + " " + k);
                    System.out.println(Math.min(dp[i-1][(j+1)%3][k], dp[i-1][(j+2)%2][k]) + " " + RGB[i][j]);
                }
            }
        }

        int answer = 1001 * N;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == j) continue;
                answer = Math.min(answer, dp[N-1][i][j]);
            }
        }

        System.out.println(answer);
    }
}
