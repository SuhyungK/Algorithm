// 수 고르기 

package Baekjoon.Gold;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon_2230 {
    
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long M = sc.nextLong();
        
        long[] sequence = new long[N];
        for (int i = 0; i < N; i++) {
            sequence[i] = sc.nextLong();
        }

        int left = 0;
        int right = 0;
        Arrays.sort(sequence);
        long minGap = Long.MAX_VALUE;
        while (left <= right && right < N) {
            System.out.println(left + " " + right);
            long gap = sequence[right] - sequence[left];
            if (gap < M) {
                right++;
                continue;
            }
            
            minGap = Math.min(minGap, gap);
            left++;
        }
        System.out.println(minGap);
    }
}
