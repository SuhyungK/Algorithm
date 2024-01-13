// 게임을 만든 동준이 

package Silver;

import java.util.Scanner;

public class baekjoon_2847 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] levels = new int[N];
        for (int i = 0; i < levels.length; i++) {
            levels[i] = sc.nextInt();
        }

        int answer = 0;
        for (int i = levels.length-1; i > 0; i--) {
            if (levels[i] > levels[i-1]) continue;
            answer += levels[i-1] - levels[i] + 1;
            levels[i-1] = levels[i] - 1;
        }

        System.out.println(answer);
    }
}
