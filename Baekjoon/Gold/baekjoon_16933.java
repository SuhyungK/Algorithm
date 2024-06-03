package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class baekjoon_16933 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		int[][] map = new int[N][M];
		for (int i = 0; i < N; i++) {
			String[] input = new StringTokenizer(br.readLine()).nextToken().split("");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(input[j]);
			}
		}

//		for (int i = 0; i < N; i++) {
//			System.out.println(Arrays.toString(map[i]));
//		}

		Queue<Node> queue = new ArrayDeque<>();
		queue.add(new Node(0, 0, 0, 1));
		boolean[][][] visited = new boolean[N][M][K+1];
		visited[0][0][0] = true;
		int[][] dir = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
		int answer = -1;
		while (!queue.isEmpty()) {
			Node cur = queue.poll();

			if (cur.x == N-1 && cur.y == M-1) {
				answer = cur.cnt;
				break;
			}

			boolean isDay = (cur.cnt % 2) == 1 ? true : false;
			for (int[] d : dir) {
				int nextX = cur.x + d[0];
				int nextY = cur.y + d[1];

				if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M) continue;

				// 제자리가 아닌 경우
				if (map[nextX][nextY] == 1) {
					// 벽인 경우
					if (isDay) {
						// 낮이면 뚫고
						if (cur.k < K && !visited[nextX][nextY][cur.k+1]) {
							visited[nextX][nextY][cur.k+1] = true;
							queue.add(new Node(nextX, nextY, cur.k + 1, cur.cnt + 1));
						}
					} else {
						// 밤이면 제자리에 있다가 다음날 낮이 되었을 때 벽을 뚫으면 됨
						queue.add(new Node(cur.x, cur.y, cur.k, cur.cnt + 1));
					}
				} else {
					// 벽이 아닌 경우
					if (!visited[nextX][nextY][cur.k]) {
						visited[nextX][nextY][cur.k] = true;
						queue.add(new Node(nextX, nextY, cur.k, cur.cnt + 1));
					}
				}
			}
		}
		System.out.println(answer);
	}

	static class Node {
		int x;
		int y;
		int k;
		int cnt;

		Node(int x, int y, int k, int cnt) {
			this.x = x;
			this.y = y;
			this.k = k;
			this.cnt = cnt;
		}
	}
}