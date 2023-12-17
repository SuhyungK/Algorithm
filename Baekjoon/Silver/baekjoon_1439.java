package Baekjoon.Silver;

import java.util.Scanner;

public class baekjoon_1439 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        
        int[] answer = new int[2];
        int a = Character.getNumericValue(S.charAt(0));
        answer[a] += 1;
        int b; 
        for (int i = 1; i < S.length(); i++) {
            b = Character.getNumericValue(S.charAt(i));
            
            if (a == b) continue;
            answer[b] += 1;
            a = b;
        }

        System.out.println(Math.min(answer[0], answer[1]));
    }
}
