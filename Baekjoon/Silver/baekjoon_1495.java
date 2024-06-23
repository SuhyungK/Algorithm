package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_1495 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] volList = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			volList[i] = Integer.parseInt(st.nextToken());
		}

		boolean[][] dp = new boolean[M+1][N+1];
		dp[S][0] = true;
		for (int j = 0; j < N; j++) {
			int vol = volList[j];

			for (int i = 0; i <= M; i++) {
				if (!dp[i][j]) continue;

				if (i + vol <= M) {
					dp[i+vol][j+1] = true;
				}

				if (i - vol >= 0) {
					dp[i-vol][j+1] = true;
				}
			}
		}

		int i = M;
		int answer = -1;
		while (i >= 0) {
			if (dp[i][N]) {
				answer = i;
				break;
			}
			i--;
		}

		System.out.println(answer);
	}

}