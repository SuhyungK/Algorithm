// 용액

package Baekjoon.Gold;

import java.util.Scanner;

public class baekjoon_2467 {
    static int N;
    static long[] values;
    static long[] binarySearch(long stdNum, int left) {
        int right = N-1;
        int mid = (left + right) / 2;
        long sum;
        long[] answer = new long[] {2_000_000_000, stdNum, values[N-1]};

        while (left <= right) {
            mid = (left + right) / 2;
            sum = stdNum + values[mid];
            if (Math.abs(sum) < answer[0]) {
                answer[0] = Math.abs(sum);
                answer[2] = values[mid];
            }

            if (sum >= 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        values = new long[N];

        for (int i = 0; i < N; i++) {
            values[i] = sc.nextLong();
        }

        long[] answer = new long[] {2_000_000_000, 0, 0};
        long[] tmp;
        for (int i = 0; i < N-1; i++) {
            tmp = binarySearch(values[i], i+1);
            if (tmp[0] <= answer[0]) {
                answer = tmp;
            }
        }

        System.out.println(answer[1] + " " + answer[2]);

    }
}
