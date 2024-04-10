// 딸기와 토마토

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_25565 {
    static int[][] garden;

    static int N;
    static int M;
    static int K;

    static List<int[]> sol(int seed) {
        List<int[]> ans = new ArrayList<>();
        if (2*K <= seed) return ans;

        // 겹치는 구간이 1칸인 경우 (가로-세로)
        if (2*K == seed+1) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (garden[i][j] == 0) continue;

                    if ((i > 0 && j > 0 && garden[i-1][j] == 1 && garden[i][j-1] == 1)
                            || (i > 0 && j < M-1 && garden[i-1][j] == 1 && garden[i][j+1] == 1)
                            || (i < N-1 && j < M-1 && garden[i+1][j] == 1 && garden[i][j+1] == 1)
                            || (i < N-1 && j > 0 && garden[i+1][j] == 1 && garden[i][j-1] == 1)) {
                        ans.add(new int[] {i+1, j+1});
                        return ans;
                    }
                }
            }
        }

        // 겹치는 구간이 1칸 이상인 경우 (가로-가로, 세로-세로)
        int len = 0;
        int s = 2*K - seed; // 겹치는 구간의 길이
        for (int i = 0; i < N; i++) {
            len = 0;
            for (int j = 0; j < M; j++) {
                if (garden[i][j] == 1) {
                    len++;

                    if (len >= K && (j == M-1 || garden[i][j+1] == 0)) {
                        // 여기서 종료

                        for (int _j = j - K + 1; _j <= j - K + s; _j++) {
                            ans.add(new int[] {i+1, _j+1});
                        }
                        return ans;
                    }
                }
            }
        }

        for (int j = 0; j < M; j++) {
            len = 0;
            for (int i = 0; i < N; i++) {
                if (garden[i][j] == 1) {
                    len++;
                }

                if (len >= K && (i == N-1 || garden[i+1][j] == 0)) {
                    // 여기서 종료
                    for (int _i = i - K + 1; _i <= i - (K-s); _i++) {
                        ans.add(new int[] {_i+1, j+1});
                    }
                    return ans;
                }
            }
        }

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        garden = new int[N+1][M+1];
        int seed = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                garden[i][j] = Integer.parseInt(st.nextToken());
                if (garden[i][j] == 1) seed++;
            }
        }

        List<int[]> ans = sol(seed);
        System.out.println(ans.size());
        for (int[] pos : ans) {
            System.out.println(pos[0] + " " + pos[1]);
        }
    }
}