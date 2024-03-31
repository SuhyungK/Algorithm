// 귀농

package Baekjoon.Gold;

import java.util.*;
import java.io.*;


public class baekjoon_1184 {
    static int N;
    static int[][] sum;
    static int[][] sum2;
    static int[][] land;

    static List<Integer> sumUpLeft(int R, int C) {
        List<Integer> tmpSum = new ArrayList<>();

        int tmp;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                tmp = sum[R][C] - sum[i][C] - sum[R][j] + sum[i][j];
                tmpSum.add(tmp);
            }
        }

        return tmpSum;
    }

    static List<Integer> sumUpRight(int R, int C) {
        List<Integer> tmpSum = new ArrayList<>();

        int tmp;
        for (int i = 0; i < R; i++) {
            for (int j = N; j > C; j--) {
                tmp = sum2[R][C] - sum2[i][C] - sum2[R][j] + sum2[i][j];
                tmpSum.add(tmp);
            }
        }

        return tmpSum;
    }

    static List<Integer> sumDownRight(int R, int C) {
        List<Integer> tmpSum = new ArrayList<>();

        int tmp;
        for (int i = N; i > R; i--) {
            for (int j = N; j > C; j--) {
                tmp = sum[i][j] - sum[i][C] - sum[R][j] + sum[R][C];
                tmpSum.add(tmp);
            }
        }

        return tmpSum;
    }

    static List<Integer> sumDownLeft(int R, int C) {
        List<Integer> tmpSum = new ArrayList<>();

        int tmp;
        for (int i = R+1; i <= N; i++) {
            for (int j = C-1; j >= 0; j--) {
                tmp = sum2[i][j] - sum2[i][C] - sum2[R][j] + sum2[R][C];
                tmpSum.add(tmp);
            }
        }

        return tmpSum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st;
        land = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                land[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        sum = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                sum[i][j] += sum[i][j-1] + land[i][j];
            }
        }

        for (int j = 1; j <= N; j++) {
            for (int i = 2; i <= N; i++) {
                sum[i][j] += sum[i-1][j];
            }
        }

        sum2 = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            for (int j = N-1; j >= 0; j--) {
                sum2[i][j] += sum2[i][j+1] + land[i][j+1];
            }
        }

        for (int j = N-1; j >= 0; j--) {
            for (int i = 1; i <= N; i++) {
                sum2[i][j] += sum2[i-1][j];
            }
        }

        List<Integer> sumList1;
        List<Integer> sumList2;
        int cnt = 0;
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < N; j++) {
                sumList1 = sumUpLeft(i, j);
                sumList2 = sumDownRight(i, j);

                for (int x : sumList1) {
                    for (int y : sumList2) {
                        if (x == y) cnt++;
                    }
                }

                sumList1 = sumUpRight(i, j);
                sumList2 = sumDownLeft(i, j);
                
                for (int x : sumList1) {
                    for (int y : sumList2) {
                        if (x == y) cnt++;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}