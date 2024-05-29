package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_1167 {
	static List<List<Node>> trees;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		trees = new ArrayList<>();
		for (int i = 0; i <= N; i++) {
			trees.add(new ArrayList<>());
		}

		StringTokenizer st;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int v = Integer.parseInt(st.nextToken());
			while (true) {
				int u = Integer.parseInt(st.nextToken());
				if (u == -1) break;
				int w = Integer.parseInt(st.nextToken());
				trees.get(v).add(new Node(u, w));
				trees.get(u).add(new Node(v, w));
			}
		}

		int nodeNum = dfs(1, 0, 0, -1, new boolean[N+1])[0];
		System.out.println(dfs(nodeNum, 0, 0, -1, new boolean[N+1])[1]);
	}

	private static int[] dfs(int cur, int curDist, int maxDist, int maxNode, boolean[] visited) {
		visited[cur] = true;
		if (maxDist < curDist) {
			maxDist = curDist;
			maxNode = cur;
		}

		for (Node node : trees.get(cur)) {
			if (visited[node.cur]) continue;
			int[] maxTmp = dfs(node.cur, curDist + node.dist, maxDist, maxNode, visited);
			maxNode = maxTmp[0];
			maxDist = maxTmp[1];
		}

		return new int[] {maxNode, maxDist};
	}

	static private class Node {
		int cur;
		int dist;

		Node(int node, int dist) {
			this.cur = node;
			this.dist = dist;
		}
	}
}