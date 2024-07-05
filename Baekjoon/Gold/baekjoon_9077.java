package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_9077 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] board = new int[10001][10001];

		int T = Integer.parseInt(br.readLine());
		while (T-- != 0) {
			int N = Integer.parseInt(br.readLine());
			while (N-- != 0) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				for (int i = x; i <= Math.min(x + 10, 10000); i++) {
					for (int j = y; j <= Math.min(y + 10, 10000); j++) {
						board[i][j]++;
					}
				}
			}

			int answer = 0;
			for (int i = 0; i <= 10000; i++) {
				for (int j = 0; j <= 10000; j++) {
					answer = Math.max(answer, board[i][j]);
					board[i][j] = 0;
				}
			}
			System.out.println(answer);
		}
	}
}
