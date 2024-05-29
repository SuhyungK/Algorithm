package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_14722 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int[][] milkCity = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				milkCity[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[][][] dp = new int[N][N][3];
		if (milkCity[0][0] == 0) {
			dp[0][0][0] = 1;
		}

		for (int i = 1; i < N; i++) {
			int t = milkCity[i][0];
			for (int k = 0; k < 3; k++) {
				dp[i][0][k] = dp[i-1][0][k];
			}
			if (dp[i-1][0][(t+2)%3] < t) continue;
			dp[i][0][t] = Math.max(dp[i-1][0][(t + 2)%3]+1, dp[i][0][t]);
		}

		for (int i = 1; i < N; i++) {
			int t = milkCity[0][i];
			for (int k = 0; k < 3; k++) {
				dp[0][i][k] = dp[0][i-1][k];
			}
			if (dp[0][i-1][(t+2)%3] < t) continue;
			dp[0][i][t] = Math.max(dp[0][i-1][(t + 2)%3]+1, dp[0][i][t]);
		}

		for (int i = 1; i < N; i++) {
			for (int j = 1; j < N; j++) {
				int t = milkCity[i][j];
				for (int k = 0; k < 3; k++) {
					dp[i][j][k] = Math.max(dp[i-1][j][k], dp[i][j-1][k]);
				}
				if (dp[i-1][j][(t+2)%3] < t && dp[i][j-1][(t+2)%3] < t) continue;
				dp[i][j][t] = Math.max(dp[i][j][(t + 2)%3]+1, dp[i][j][t]);
			}
		}

//		for (int i = 0; i < N; i++) {
//			for (int j = 0; j < N; j++) {
//				System.out.print(Arrays.toString(dp[i][j]) + " ");
//			}
//			System.out.println();
//		}
		System.out.println(Arrays.stream(dp[N - 1][N - 1]).max().getAsInt());;
	}
}