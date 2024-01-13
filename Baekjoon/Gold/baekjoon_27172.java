// 수 나누기 게임

import java.io.*;
import java.util.*;

public class baekjoon_27172 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] cards = new int[N];
        Map<Integer, Integer> score = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
            score.put(cards[i], 0);
        }

        for (int i = 0; i < N; i++) {
            int x = cards[i];
            for (int j = 2 * x; j < 1_000_001; j += x) {
                if (score.containsKey(j)) {
                    score.put(j, score.get(j) - 1);
                    score.put(x, score.get(x) + 1);
                }
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.print(score.get(cards[i]) + " ");
        }
    }
}