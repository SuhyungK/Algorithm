// 두 수의 합

package Baekjoon.Silver;

import java.util.*;
import java.io.*;

public class baekjoon_3273 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int x = Integer.parseInt(br.readLine());

        int left = 0;
        int right = n - 1;
        int sum = 0;
        int answer = 0;
        while (left < right) {
            sum = arr[left] + arr[right];
            if (sum == x) {
                answer++;
                left++;
                right--;
            } else if (sum < x) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(answer);
    }
}