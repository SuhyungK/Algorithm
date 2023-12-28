// 부분합 

package Baekjoon.Gold;

import java.util.Scanner;

public class baekjoon_1806 {
        static int N, S;
    static int[] arr;
    static int sol(int s) {
        if (s < S) {
            return 0;
        }

        s = 0;
        int i = 0, j = 0, minLen = arr.length;
        while (true) {
            if (s >= S) {
                // 기준을 충족하는 경우 1. 왼쪽 값을 빼고, 2. 왼쪽 인덱스 증가
                s -= arr[i];
                minLen = Math.min(minLen, j - i);
                i++;
            } else {
                // 기준을 충족하지 않는 경우. 1. 오른쪽 값을 더하고, 2. 오른쪽 인덱스 증가
                if (j >= arr.length) break;
                s += arr[j];
                j++;
            }
        }
        return minLen;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        S = sc.nextInt();

        arr = new int[N];
        int s = 0;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
            s += arr[i];
        }

        System.out.println(sol(s));
    }
}
