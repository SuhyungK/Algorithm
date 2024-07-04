package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_2186 {
	static int N;
	static int M;
	static int K;
	static String[][] board;
	static String[] word;
	static int[][] dir = new int[][] {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		board = new String[N][M];
		for (int i = 0; i < N; i++) {
			board[i] = br.readLine().split("");
		}

		word = br.readLine().split("");
		int[][][] dp = new int[word.length][N][M];
		for (int i = 0; i < word.length; i++) {
			for (int j = 0; j < N; j++) {
				Arrays.fill(dp[i][j], -1);
			}
		}

		int answer = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (board[i][j].equals(word[0])) {
					dp[0][i][j] = dfs(0, i, j, dp);
					answer += dp[0][i][j];
				}
			}
		}
		System.out.println(answer);
	}

	static int dfs(int idx, int x, int y, int[][][] dp) {
		if (idx == word.length - 1) {
			dp[idx][x][y] = 1;
		}

		if (dp[idx][x][y] != -1) {
			return dp[idx][x][y];
		}

		dp[idx][x][y] = 0;
		for (int[] xy : dir) {
			for (int k = 1; k <= K; k++) {
				int nx = x + xy[0] * k;
				int ny = y + xy[1] * k;

				if (isBound(nx, ny) && word[idx+1].equals(board[nx][ny])) {
					// 좌표가 범위 내에 있고, 다음에 찾아야 할 문자가 일치할 경우
					dp[idx][x][y] += dfs(idx + 1, nx, ny, dp);
				}
			}

		}

		return dp[idx][x][y];
	}

	private static boolean isBound(int x, int y) {
		return 0 <= x && x < N && 0 <= y && y < M;
	}
}
