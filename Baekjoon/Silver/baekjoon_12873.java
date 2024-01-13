// 기념품

package Silver;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class baekjoon_12873 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            list.add(i + 1);
        }

        int t = 1;
        int idx = 0;
        while (list.size() > 1) {
            idx = (int) ((idx + Math.pow(t, 3) - 1) % list.size());
            list.remove(idx);
            t++;
        }

        System.out.println(list.get(0));
    }
}
