// 막대기 

package Baekjoon.Bronze;

import java.util.Scanner;

public class baekjoon_17608 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] bar = new int[N];
        
        for (int i = 0; i < bar.length; i++) {
            bar[i] = sc.nextInt();
        }

        int barHeight = bar[bar.length-1];
        int count = 1;
        for (int i = bar.length-1; i > -1; i--) {
            if (bar[i] > barHeight) {
                barHeight = bar[i];
                count++;
            }
        }

        System.out.println(count);
    }
    
}
