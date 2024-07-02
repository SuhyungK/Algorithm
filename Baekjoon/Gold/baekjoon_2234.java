package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_2234 {
	static int N;
	static int M;
	static int[][] walls;
	static Map<Integer, Integer> room = new HashMap<>();
	static int[][] dir = new int[][] {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		walls = new int[M][N];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				walls[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 방 개수 세
		int[][] visited = new int[M][N];
		int num = 1;
		int count = 0;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (visited[i][j] == 0) {
					count = bfs(i, j, visited, num);
					room.put(num, count);
					num++;
				}
			}
		}

		// 방 합쳐보기
		int answer = 0;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				int wall = walls[i][j];

				for (int k = 0; k < 4; k++) {
					if ((wall & (1 << k)) != 0) {
						// 벽이 있으면 없애고 그 방향으로 갔을 때
						int ni = i + dir[k][0];
						int nj = j + dir[k][1];


						if (isBound(ni, nj) && visited[i][j] != visited[ni][nj]) {
							answer = Math.max(answer, room.get(visited[i][j]) + room.get(visited[ni][nj]));
						}
					}
				}
			}
		}

		System.out.println(room.size());
		System.out.println(Collections.max(room.values()));
		System.out.println(answer);
	}


	static int bfs(int startX, int startY, int[][] visited, int num) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {startX, startY});
		visited[startX][startY] = num;
		int count = 1;
		while (!queue.isEmpty()) {
			int[] node = queue.poll();
			int wall = walls[node[0]][node[1]];

			for (int k = 0; k < 4; k++) {
				if ((wall & (1 << k)) == 0) {
					// 현재 방향으로 벽이 없
					int nextX = node[0] + dir[k][0];
					int nextY = node[1] + dir[k][1];

					if (isBound(nextX, nextY) && visited[nextX][nextY] == 0) {
						queue.add(new int[] {nextX, nextY});
						visited[nextX][nextY] = num;
						count++;
					}
				}
			}
		}

		return count;
	}

	private static boolean isBound(int x, int y) {
		return 0 <= x && x < M && 0 <= y && y < N;
	}
}