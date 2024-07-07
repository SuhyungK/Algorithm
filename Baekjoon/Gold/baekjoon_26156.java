package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_26156 {
	static int D = 1_000_000_007;
	static char[] TARGET_STR = new char[] {'R', 'O', 'C', 'K'};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		char[] str = br.readLine().toCharArray();

		int[][] dp = new int[5][N+1];
		dp[0][1] = 1;
		for (int i = 2; i <= N; i++) {
			dp[0][i] = (dp[0][i-1] * 2) % D;
		}

		for (int i = 1; i <= 4; i++) {
			char target = TARGET_STR[i-1];
			for (int j = 1; j <= N; j++) {
				dp[i][j] = (dp[i][j-1]) % D;
				if (target == str[j-1]) {
					dp[i][j] += (dp[i-1][j]) % D;
				}
			}
		}
		System.out.println(dp[4][N] % D);
	}
}