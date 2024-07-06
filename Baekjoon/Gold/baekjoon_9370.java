package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_9370 {
	static BufferedReader br;
	static StringTokenizer st;
	static int n, m, t, s, g, h;
	static List<List<int[]>> graph;
	static int[] targets;
	static int[][] dist;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		while (T-- != 0) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			g = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());

			graph = new ArrayList<>();
			for (int i = 0; i <= n; i++) {
				graph.add(new ArrayList<>());
			}

			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int d = Integer.parseInt(st.nextToken());

				graph.get(a).add(new int[] {b, d});
				graph.get(b).add(new int[] {a, d});
			}

			targets = new int[t];// 목적지 후
			for (int i = 0; i < t; i++) {
				targets[i] = Integer.parseInt(br.readLine());
			}

			solution(s);
		}

		System.out.println(sb.toString());
	}

	static void solution(int s) {
		dist = new int[2][graph.size()];
		Arrays.fill(dist[0], 10_000_000);
		dist[0][s] = 0;

		PriorityQueue<Road> pq = new PriorityQueue<>();
		boolean visited = false;
		pq.offer(new Road(s, 0, visited));
		while (!pq.isEmpty()) {
			Road cur = pq.poll();

			if (dist[0][cur.x] < cur.d) continue;
			for (int[] next : graph.get(cur.x)) {
				visited = cur.visited;

				if ((cur.x == g && next[0] == h) || (next[0] == g && cur.x == h)) visited = true;
				if (dist[0][next[0]] > cur.d + next[1]) {
					// 최단거리로 갱신 가능한 경우
					dist[0][next[0]] = cur.d + next[1];
					dist[1][next[0]] = visited ? 1 : 0;
					pq.offer(new Road(next[0], cur.d + next[1], visited));
				} else if (dist[1][next[0]] == 0 && visited && dist[0][next[0]] == cur.d + next[1]) {
					dist[1][next[0]] = 1;
					pq.offer(new Road(next[0], cur.d + next[1], visited));
				}
			}
		}

		Arrays.sort(targets);
		for (int target : targets) {
			if (dist[1][target] == 1) {
				sb.append(target + " ");
			}
		}
		sb.append("\n");
	}

	static class Road implements Comparable<Road>{
		int x; // 위치
		int d; // 거리
		boolean visited;

		Road(int e, int d, boolean visited) {
			this.x = e;
			this.d = d;
			this.visited = visited;
		}

		@Override
		public int compareTo(Road road) {
			return this.d - road.d;
		}

		public String toString() {
			return x + " " + d;
		}
	}
}
