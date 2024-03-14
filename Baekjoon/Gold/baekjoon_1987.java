import java.util.*;
import java.io.*;

public class baekjoon_1987 {
    static char[][] board;
    static int answer = 0;
    static boolean[] alpha = new boolean[26];
    static int R;
    static int C;
    static final int GAP = 'A';
    static int[][] direction = new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        
        board = new char[R][C];
        for (int i = 0; i < R; i++) {
            board[i] = sc.next().toCharArray();
        }
        
        alpha[board[0][0] - GAP] = true;
        
        dfs(0, 0, 1);
        System.out.println(answer);
    }

    private static void dfs(int x, int y, int count) {
        answer = Math.max(answer, count);

        int nx; 
        int ny;
        char a;
        for (int i = 0; i < 4; i++) {
            nx = x + direction[i][0];
            ny = y + direction[i][1];
            
            if (nx < 0 || ny < 0 || nx >= R || ny >= C || alpha[board[nx][ny] - GAP]) continue;
            a = board[nx][ny];
            alpha[a - GAP] = true;
            dfs(nx, ny, count+1);
            alpha[a - GAP] = false;
        }
    }
}