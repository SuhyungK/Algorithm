package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_14238 {
	static String answer = "-1";
	static boolean[][][][][] dp = new boolean[51][51][51][3][3];
	static int L;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();

		int[] cnt = new int[3];
		for (char s : input.toCharArray()) {
			cnt[s - 65]++;
		}

		dfs(cnt[0], cnt[1], cnt[2], 0, 0, "");
		System.out.println(answer);
	}

	static boolean dfs(int a, int b, int c, int prev, int pprev, String record) {
		if (a == 0 && b == 0 && c == 0) {
			answer = record;
			return true;
		}

		if (dp[a][b][c][prev][pprev]) return false;
		dp[a][b][c][prev][pprev] = true;

		if (a > 0) {
			if (dfs(a - 1, b, c, 0, prev, record + "A")) return true;
		}

		if (b > 0 && prev != 1) {
			if (dfs(a, b - 1, c, 1, prev, record + "B")) return true;
		}

		if (c > 0 && prev != 2 && pprev != 2) {
			if (dfs(a, b, c - 1, 2, prev, record + "C")) return true;
		}

		return false;
	}
}
