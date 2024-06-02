package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_1561 {
	static long N;
	static int M;
	static int[] rides;
	static int last = -1;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		rides = new int[M];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			rides[i] = Integer.parseInt(st.nextToken());
		}

		long last = N;
		if (N > M) {
			long maxTime = N * 30;
			long minTime = 0;
			while (minTime <= maxTime) {
				long midTime = (maxTime + minTime) / 2;

				if (binarySearch(N, midTime)) {
					maxTime = midTime - 1;
					last = findLast(N, midTime);
				} else {
					minTime = midTime + 1;
				}
			}
		}
		System.out.println(last);
	}

	static private boolean binarySearch(long N, long time) {
		for (int i = 0; i < rides.length; i++) {
			N -= (time / rides[i]) + 1;
		}
		return N <= 0;
	}

	static private int findLast(long cnt, long time) {
		for (int i = 0; i < rides.length; i++) {
			cnt -= ((time-1) / rides[i]) + 1;
		}

		System.out.println("time, cnt " + time + " " + cnt);

		for (int i = 0; i < rides.length; i++) {
			if (time % rides[i] == 0) {
				cnt--;
				if (cnt == 0) return i+1;
			}
		}
		return -1;
	}
}