package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class baekjoon_1300 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());

		int maxBound = K;
		int minBound = 1;
		while (minBound <= maxBound) {
			int mid = (maxBound + minBound) / 2;

			int count = 0;
			for (int i = 1; i <= N; i++) {
				count += Math.min(N, mid / i);
			}

			if (count < K) {
				minBound = mid + 1;
			} else {
				maxBound = mid - 1;
			}
		}
		System.out.println(minBound);
	}

}