package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class baekjoon_1175 {
	static int N;
	static int M;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		char[][] room = new char[N][M];
		for (int i = 0; i < N; i++) {
			room[i] = br.readLine().toCharArray();
		}

		System.out.println(bfs(room));
	}

	static int bfs(char[][] room) {
		Queue<Node> queue = new LinkedList<>();
		Node start = findStart(room, 'S');
		findEnd(room, 'C');
		queue.add(start);
		int[][] dxy = new int[][] {{0, 1}, {-1, 0}, {1, 0}, {0, -1}};
		int[][][][] visited = new int[N][M][4][4];
		while (!queue.isEmpty()) {
			Node cur = queue.poll();

			for (int k = 0; k < 4; k++) {
				int nx = cur.x + dxy[k][0];
				int ny = cur.y + dxy[k][1];

				if (nx < 0 || ny < 0 || nx >= N || ny >= M || room[nx][ny] == '#' || cur.dir == k) continue;
				if (cur.dir == -1) cur.dir = 0;

				char nextChar = room[nx][ny];
				if ((cur.bit == 1 && nextChar == 'C')
						|| (cur.bit == 2 && nextChar == 'D')) {
					return visited[cur.x][cur.y][cur.dir][cur.bit] + 1;
				}
				int nbit = cur.bit;
				if (nextChar == 'C') {
					nbit = 2;
				} else if (nextChar == 'D') {
					nbit = 1;
				}

				if (visited[nx][ny][k][nbit] == 0) {
					visited[nx][ny][k][nbit] = visited[cur.x][cur.y][cur.dir][cur.bit] + 1;
					queue.add(new Node(nx, ny, k, nbit));
				}
			}
		}
		return -1;
	}

	private static Node findStart(char[][] graph, char target) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j] == target) {
					graph[i][j] = '.';
					return new Node(i, j, -1, 0);
				}
			}
		}
		return null;
	}

	private static void findEnd(char[][] graph, char target) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j] == target) {
					graph[i][j] = 'D';
					return;
				}
			}
		}
	}

	static class Node {
		int x;
		int y;
		int dir;
		int bit;

		Node(int x, int y, int dir, int bit) {
			this.x = x;
			this.y = y;
			this.dir = dir;
			this.bit = bit;
		}
	}
}