import java.util.Scanner;

public class Solution {
    static Scanner sc;

    private static int solution() {
        int n = sc.nextInt();

        int[][] arr = new int[100][100];
        // 배열 입력
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        int deadlockCount = 0;
        for (int col = 0; col < 100; col++) {
            boolean nPoleOn = false;
            for (int row = 0; row < 100; row++) {
                if (arr[row][col] == 1) {
                    nPoleOn = true;
                } else if (nPoleOn == true && arr[row][col] == 2) {
                    nPoleOn = false;
                    deadlockCount++;
                }
            }
        }
        return deadlockCount;
    }

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        for (int t = 1; t < 11; t++) {
            System.out.println(solution());
        }
    }
}
