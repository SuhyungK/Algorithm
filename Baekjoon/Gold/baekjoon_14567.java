// 선수 과목 

import java.io.*;
import java.util.*;

public class baekjoon_14567 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] terms = new int[N+1];
        int[] prerequisite = new int[N+1];
        Map<Integer, List<Integer>> subjects = new HashMap<>();
        for (int i = 0; i < M; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            
            if (!subjects.containsKey(A)) {
                subjects.put(A, new ArrayList<>());
            }
            subjects.get(A).add(B);
            prerequisite[B]++;
        }

        Queue<int[]> queue = new LinkedList<>();
        
        for (int i = 1; i < N+1; i++) {
            if (prerequisite[i] == 0) {
                queue.add(new int[]{i, 0});
            }
        }

        while (!queue.isEmpty()) {
            int[] subInfo = queue.poll();
            
            int subNum = subInfo[0];
            int term = ++subInfo[1];
            terms[subNum] = term;
            if (subjects.getOrDefault(subNum, null) != null) {
                for (int nextSubNum : subjects.get(subNum)) {
                    prerequisite[nextSubNum]--;
                    if (prerequisite[nextSubNum] == 0) {
                        queue.add(new int[]{nextSubNum, term});
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N+1; i++) {
            sb.append(terms[i] + " ");
        }

        System.out.println(sb);
    }
}
