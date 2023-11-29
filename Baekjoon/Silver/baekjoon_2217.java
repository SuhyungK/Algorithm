// 로프

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class baekjoon_2217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        int[] rope = new int[N];
        for (int i = 0; i < rope.length; i++) {
            rope[i] = Integer.parseInt(br.readLine());
        }

        rope = Arrays.stream(rope).boxed().sorted(Collections.reverseOrder()).mapToInt(Integer::intValue).toArray();
        
        int max_weight = 0;
        for (int i = 0; i < rope.length; i++) {
            int tmp = rope[i] * (i+1);
            if (max_weight < tmp) {
                max_weight = tmp;
            }
        }
        System.out.println(max_weight);
    }
}