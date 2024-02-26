// 게임

package Baekjoon.Silver;

import java.io.IOException;
import java.util.Scanner;

public class baekjoon_1072 {
        static int transform(double X, double Y) {
        return (int) ((100 * Y / X));
    }
    
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        long X = sc.nextLong();
        long Y = sc.nextLong();

        int oddOfWinning = transform(X, Y);
        if (oddOfWinning >= 99) {
            System.out.println(-1);
        } else {
            long high = Long.MAX_VALUE;
            long low = 0;
    
            while (low <= high) {
                long mid = (low + high) / 2;
    
                if (transform(X + mid, Y + mid) > oddOfWinning) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
    
            System.out.println(low);
        }
    }
}
