// 거북이

package Silver;

import java.util.Scanner;

public class baekjoon_8911 {
    static int[][] direction = new int[][] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    static int solution(String orders) {
        int maxX = Integer.MIN_VALUE;
        int minX = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int dirNum = 0;
        int x = 0;
        int y = 0;
        maxX = Math.max(maxX, x);
        minX = Math.min(minX, x);
        maxY = Math.max(maxY, y);
        minY = Math.min(minY, y);
        for (char dir : orders.toCharArray()) {
            if (dir == 'F') {
                x += direction[dirNum][0];
                y += direction[dirNum][1];
            } else if (dir == 'B') {
                x += direction[(dirNum + 2) % 4][0];
                y += direction[(dirNum + 2) % 4][1];
            } else if (dir == 'L') {
                dirNum = (dirNum + 3) % 4;
            } else if (dir == 'R') {
                dirNum = (dirNum + 1) % 4;
            }
            maxX = Math.max(maxX, x);
            minX = Math.min(minX, x);
            maxY = Math.max(maxY, y);
            minY = Math.min(minY, y);
            // System.out.println(x + " " + y);
        }
        return (maxX - minX) * (maxY - minY);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            System.out.println(solution(sc.next()));
        }

    }
}