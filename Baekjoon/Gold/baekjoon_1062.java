// 가르침

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_1062 {
    static final int[] INIT = new int[] {'a', 'c', 'i', 't', 'n'};
    static String[] words;
    static int answer = 0;
    static int check(String word, boolean[] learn) {
        for (int i = 4; i < word.length() - 4; i++) {
            if (!learn[word.charAt(i) - 97]) {
                return 0;
            }
        }
        return 1;
    }

    static void dfs(int i, int k, boolean[] learn) {
        if (k == 0) {
            int tmp = 0;
            for (int j = 0; j < words.length; j++) {
                tmp += check(words[j], learn);
            }
            answer = Math.max(answer, tmp);
            return;
        }

        if (i == 25) return;
        for (int j = i+1; j < 26; j++) {
            if (learn[j]) continue;
            learn[j] = true;
            dfs(j, k-1, learn);
            learn[j] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        boolean[] learn = new boolean[26];
        for (int i = 0; i < INIT.length; i++) {
            learn[INIT[i] - 97] = true;
        }

        if (K >= 5) {
            dfs(0, K-5, learn);
        }
        System.out.println(answer);
    }
}