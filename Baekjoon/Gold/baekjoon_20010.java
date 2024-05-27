package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_20010 {
	static int N;
	static int K;
	static int[] parent;
	static List<List<Node>> mst;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		List<Route> routes = new ArrayList<>();
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			routes.add(new Route(a, b, c));
		}

		parent = new int[N];
		for (int i = 0; i < N; i++) {
			parent[i] = i;
		}

		int count = 0;
		int cost = 0;
		Collections.sort(routes);
		mst = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			mst.add(new ArrayList<>());
		}

		for (Route route : routes) {
			if (count == N-1) break;
			int a = route.a;
			int b = route.b;
			int x = find(a);
			int y = find(b);

			if (find(x) != find(y)) {
				union(x, y);
				cost += route.c;
				mst.get(a).add(new Node(b, route.c));
				mst.get(b).add(new Node(a, route.c));
				count++;
			}
		}

		System.out.println(cost);
		int nodeNum = dfs(0, 0, 0, -1, new boolean[N])[0];
		System.out.println(dfs(nodeNum, 0, 0, -1, new boolean[N])[1]);
	}

	private static int[] dfs(int cur, int curCost, int maxCost, int maxNode, boolean[] visited) {
		visited[cur] = true;
		if (maxCost < curCost) {
			maxCost = curCost;
			maxNode = cur;
		}

		for (Node node : mst.get(cur)) {
			if (visited[node.x]) continue;
			int[] maxTmp = dfs(node.x, curCost + node.cost, maxCost, maxNode, visited);
			maxNode = maxTmp[0];
			maxCost = maxTmp[1];
		}

		return new int[] {maxNode, maxCost};
	}

	private static int find(int x) {
		if (parent[x] != x) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}

	private static void union(int x, int y) {
		x = find(x);
		y = find(y);

		if (x <= y) {
			parent[y] = x;
		} else {
			parent[x] = y;
		}
	}

	static class Route implements Comparable<Route> {
		int a;
		int b;
		int c;

		Route(int a, int b, int c) {
			this.a = a;
			this.b = b;
			this.c = c;
		}

		@Override
		public int compareTo(Route o) {
			return this.c - o.c;
		}
	}

	static class Node {
		int x;
		int cost;

		Node(int x, int cost) {
			this.x = x;
			this.cost = cost;
		}
	}
}