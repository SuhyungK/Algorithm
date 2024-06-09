package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_2565 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int[][] lines = new int[N][2];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			lines[i][0] = Integer.parseInt(st.nextToken());
			lines[i][1] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(lines, (o1, o2) -> {
			if (o1[0] == o2[0]) return o1[1] - o2[1];
			return o1[0] - o2[0];
		});

		List<Integer> wires = new ArrayList<>();
		for (int[] line : lines) {
			int left = 0;
			int right = wires.size() - 1;
			while (left <= right) {
				int mid = (left + right) / 2;

				if (wires.get(mid) > line[1]) {
					right = mid - 1;
				} else {
					left = mid + 1;
				}
			}

			if (wires.size() > left) {
				wires.set(left, line[1]);
			} else {
				wires.add(line[1]);
			}
		}

		System.out.println(N - wires.size());
	}
}