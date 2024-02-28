// 꼬인 전깃줄

package Baekjoon.Gold;

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class baekjoon_1365 {
        static int binarySearch(int x, int[] arr, int rightIdx) {
        int leftIdx = 0;
        int midIdx;
        while (leftIdx <= rightIdx) {
            midIdx = (leftIdx + rightIdx) / 2;

            if (arr[midIdx] < x) {
                leftIdx = midIdx + 1;
            } else {
                rightIdx = midIdx - 1;
            }
        }
        
        arr[leftIdx] = x;
        return leftIdx;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] telephonePole = new int[N];
        Arrays.fill(telephonePole, Integer.MAX_VALUE);

        telephonePole[0] = sc.nextInt();
        int maxLength = 0;
        for (int i = 0; i < N-1; i++) {
            int inputNumber = sc.nextInt();
            int idx = binarySearch(inputNumber, telephonePole, maxLength);
            maxLength = Math.max(idx, maxLength);
        }

        System.out.println(N - maxLength - 1);
    }
}
