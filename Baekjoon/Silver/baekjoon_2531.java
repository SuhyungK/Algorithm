package Baekjoon.Silver;

import java.util.*;
import java.io.*;

public class baekjoon_2531 {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] belt = new int[N+1];
        for (int i = 0; i < N; i++) {
            belt[i] = Integer.parseInt(br.readLine());
        }

        int[] count = new int[d+1];

        int left = 0;
        int right = 0;
        int plateCount = 0;
        for (int i = 0; i < k; i++) {
            int curPlate = belt[right];
            count[curPlate]++;
            if (count[curPlate] == 1) {
                plateCount++;
            }
            right++;
        }

        int maxPlateCount = plateCount + (count[c] == 0 ? 1 : 0);
        while (true) {
            if (left == N) break;
            int curPlate = belt[right%N];
            count[curPlate]++;
            if (count[curPlate] == 1) {
                plateCount++;
            }
            right++;

            int lastPlate = belt[left%N];
            count[lastPlate]--;
            if (count[lastPlate] == 0) {
                plateCount--;
            }
            left++;

            maxPlateCount = Math.max(maxPlateCount, plateCount + (count[c] == 0 ? 1 : 0));
        }
        System.out.println(maxPlateCount);
    }
}
