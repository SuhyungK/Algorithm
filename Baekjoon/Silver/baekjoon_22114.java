package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_22114 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int[] L = new int[N-1];
		for (int i = 0; i < N-1; i++) {
			L[i] = Integer.parseInt(st.nextToken());
		}

		int[][] dp = new int[2][N];
		Arrays.fill(dp[0], 1);

		int answer = 0;
		for (int i = 0; i < N-1; i++) {
			int k = L[i];

			if (k > K) {
				// 점프 해야 될 때
				dp[1][i+1] = dp[0][i] + 1;
				answer = Math.max(answer, dp[1][i]);
			} else {
				// 점프 안 해도 될 때
				dp[0][i+1] = dp[0][i] + 1;
				dp[1][i+1] = dp[1][i] + 1;
			}
		}

		int endMax = Math.max(dp[0][N-1], dp[1][N-1]);
		System.out.println(Math.max(answer, endMax));
	}
}
