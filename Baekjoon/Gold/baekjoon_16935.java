// 배열 돌리기 3

package Baekjoon.Gold;

import java.util.Scanner;

public class baekjoon_16935 {
    static int[][] one (int[][] arr, int N, int M) {
        int[][] tmpArr = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                tmpArr[i][j] = arr[N - i- 1][j];
            }
        }
        return tmpArr;
    }

    static int[][] two(int[][] arr, int N, int M) {
        int[][] tmpArr = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                tmpArr[i][j] = arr[i][M - j - 1];
            }
        }
        return tmpArr;
    }

    static int[][] three(int[][] arr, int N, int M) {
        int[][] tmpArr = new int[M][N];
        for (int j = 0; j < M; j++) {
            int[] tmp = new int[N];
            for (int i = 0; i < N; i++) {
                tmp[i] = arr[N - i - 1][j];
            }
            tmpArr[j] = tmp;
        }
        return tmpArr;
    }

    static int[][] four(int[][] arr, int N, int M) {
        int[][] tmpArr = new int[M][N];
        for (int j = 0; j < M; j++) {
            int[] tmp = new int[N];
            for (int i = 0; i < N; i++) {
                // System.out.println(i + " " + j);
                tmp[i] = arr[i][M - j - 1];
            }
            tmpArr[j] = tmp;
        }
        return tmpArr;
    }

    static int[][] five(int[][] arr, int N, int M) {
        int[][] tmpArr = new int[N][M];
        int n = N / 2;
        int m = M / 2;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (i < n && j < m) { // 1번
                    tmpArr[i][j + m] = arr[i][j];
                } else if (i < n && j >= m) { // 2번
                    tmpArr[i + n][j] = arr[i][j];
                } else if (j >= m) { // 3번
                    tmpArr[i][j - m] = arr[i][j];
                } else { // 4번
                    tmpArr[i - n][j] = arr[i][j];
                }
            }
        }
        return tmpArr;
    }

    static int[][] six(int[][] arr, int N, int M) {
        int[][] tmpArr = new int[N][M];
        int n = N / 2;
        int m = M / 2;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (i < n && j < m) { // 1번
                    tmpArr[i + n][j] = arr[i][j];
                } else if (i < n && j >= m) { // 2번
                    tmpArr[i][j - m] = arr[i][j];
                } else if (j >= m) { // 3번
                    tmpArr[i - n][j] = arr[i][j];
                } else { // 4번
                    tmpArr[i][j + m] = arr[i][j];
                }
            }
        }
        return tmpArr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int R = sc.nextInt();
        
        // 배열 입
        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        
        int r;
        for (int k = 0; k < R; k++) {
            r = sc.nextInt();
            
            if (r == 1) arr = one(arr, N, M);
            else if (r == 2) arr = two(arr, N, M);
            else if (r == 3) arr = three(arr, N, M);
            else if (r == 4) arr = four(arr, N, M);
            else if (r == 5) arr = five(arr, N, M);
            else if (r == 6) arr = six(arr, N, M);
            N = arr.length;
            M = arr[0].length;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }   
}
