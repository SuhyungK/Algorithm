// Dance Dance Revolution

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_2342 {
    static int getPower(int s, int e) {
        if (s == 0) return 2;
        if (s == e) return 1;

        if (s == 1) {
            if (e == 3) return 4;
            else return 3;
        } else if (s == 2) {
            if (e == 4) return 4;
            else return 3;
        } else if (s == 3) {
            if (e == 1) return 4;
            else return 3;
        } else {
            if (e == 2) return 4;
            else return 3;
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        List<Integer> arr = new ArrayList<>();
        int input;
        while (true) {
            input = sc.nextInt();
            if (input == 0) break;
            arr.add(input);
        }

        int N = arr.size();
        if (N == 0) System.out.println(0);
        if (N > 0) {
            int[][][] dp = new int[N][5][5];
    
            int next = arr.get(0);
            int left;
            int right;
            int score;
            dp[0][next][0] = 2;
            dp[0][0][next] = 2;
            for (int i = 0; i < N-1; i++) {
                next = arr.get(i+1);
                for (int j = 0; j < 5; j++) {
                    for (int k = 0; k < 5; k++) {
                        score = dp[i][j][k];
                        if (dp[i][j][k] == 0) continue;
                        
                        left = getPower(j, next);
                        right = getPower(k, next);
                        
                        if (dp[i+1][next][k] == 0) {
                            dp[i+1][next][k] = score + left;
                        } else {
                            dp[i+1][next][k] = Math.min(dp[i+1][next][k], score + left);
                        }
                        
                        if (dp[i+1][j][next] == 0) {
                            dp[i+1][j][next] = score + right;
                        } else {
                            dp[i+1][j][next] = Math.min(dp[i+1][j][next], score + right);
                        }
                    }
                }
            }
            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < 5; j++) {
                    System.out.println(Arrays.toString(dp[i][j]));
                }
                System.out.println();
            }
            int answer = Integer.MAX_VALUE;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (dp[N-1][i][j] == 0) continue;
                    answer = Math.min(answer, dp[N-1][i][j]);
                }
            }
    
            System.out.println(answer);
        }
    }
}