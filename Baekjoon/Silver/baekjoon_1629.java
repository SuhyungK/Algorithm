package Baekjoon.Silver;

import java.io.IOException;
import java.util.Scanner;


public class baekjoon_1629 {
    static long multi(int x, int A, int C) {

        if (x == 1) return A % C;

        long tmp = multi(x / 2, A, C);
        if (x % 2 == 1) {
            return (tmp * tmp % C) * A % C;
        }

        return tmp * tmp % C;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        System.out.println(multi(B, A, C) % C);
    }
}