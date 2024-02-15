// 주몽

package Baekjoon.Silver;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon_1940 {
        public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int left = 0;
        int right = N-1;
        int answer = 0;
        while (left < right && right < N) {
            int sum = arr[left] + arr[right];
            if (sum == M) {
                answer++;
                left++;
                right--;
            } else if (sum < M) {
                left++;
            } else {
                right--;
            }
        }
        System.out.println(answer);
    }
}
