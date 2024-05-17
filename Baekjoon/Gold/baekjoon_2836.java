package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_2836 {
	static int N;
	static int M;

	static long sol(List<Route> routes) {
		if (routes.isEmpty()) {
			return 0;
		}

		long length = 0;
		int start = 0;
		int end = 0;
		for (Route route : routes) {
			if (end < route.start) {
				length += (end - start) * 2L;
				start = route.start;
				end = route.end;
			} else {
				end = Math.max(end, route.end);
			}
		}
		return length + (end - start) * 2L;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		List<Route> routes = new ArrayList();
		for (int i = 0; i <  N; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			if (e < s) {
				routes.add(new Route(e, s)); // 역방향으로 넣
			}

		}
		Collections.sort(routes);
		System.out.println(M + sol(routes));
	}

	static class Route implements Comparable<Route>{
		int start;
		int end;

		public Route(int start, int end) {
			this.start = start;
			this.end = end;
		}

		@Override
		public int compareTo(Route r) {
			return this.start - r.start;
		}
	}
}