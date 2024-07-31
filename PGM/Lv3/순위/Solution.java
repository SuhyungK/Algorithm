package PGM.Lv3.순위;

import java.util.*;

public class Solution {
    public int solution(int n, int[][] results) {
        List<List<Integer>> graph = new ArrayList<>();
        List<List<Integer>> reverseGraph = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
            reverseGraph.add(new ArrayList<>());
        }

        for (int[] res : results) {
            graph.get(res[0]).add(res[1]);
            reverseGraph.get(res[1]).add(res[0]);
        }

        List<Set<Integer>> win = new ArrayList<>();
        List<Set<Integer>> lose = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            win.add(new HashSet<>());
            lose.add(new HashSet<>());
        }

        boolean[] winVisited = new boolean[n+1];
        boolean[] loseVisited = new boolean[n+1];
        for (int i = 1; i <= n; i++) {
            traversal(i, graph, win, winVisited);
            traversal(i, reverseGraph, lose, loseVisited);
        }

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            // System.out.println(i + " " + win.get(i) + " " + lose.get(i));

            win.get(i).remove(i);
            lose.get(i).remove(i);
            if (win.get(i).size() + lose.get(i).size() == n - 1) {
                answer++;
            }
            System.out.println(i + " " + win.get(i) + " " + lose.get(i));
        }
        return answer;
    }

    Set<Integer> traversal(int cur, List<List<Integer>> graph, List<Set<Integer>> result, boolean[] visited) {
        if (visited[cur]) return result.get(cur);

        visited[cur] = true;
        result.get(cur).add(cur);
        for (int next : graph.get(cur)) {
            result.get(cur).addAll(traversal(next, graph, result, visited));
        }
        return result.get(cur);
    }
}
