package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class baekjoon_9251 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] A = br.readLine().split("");
		String[] B = br.readLine().split("");

		int N = A.length;
		int M = B.length;
		int[][] dp = new int[N+1][M+1];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (A[i].equals(B[j])) {
					dp[i+1][j+1] = dp[i][j] + 1;
				} else {
					dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
				}
			}
		}

		System.out.println(dp[N][M]);
	}
}