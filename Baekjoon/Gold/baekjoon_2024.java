// 선분 덮기

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_2024 {
    static int M;
    static int sol(List<Line> lines) {
        Collections.sort(lines);
        if (lines.size() == 0) return 0;

        int answer = 0;
        int end = 0;
        int maxEnd = end;
        for (Line line : lines) {
            if (maxEnd >= M) {
                return ++answer;
            }

            if (end < line.s) {
                if (maxEnd == end) {
                    return 0;
                }
                end = maxEnd;
                answer++;
            }
            maxEnd = Math.max(maxEnd, line.e);
        }

        if (maxEnd >= M) {
            return ++answer;
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        M = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int L;
        int R;
        List<Line> lines = new ArrayList<>();
        while (true) {
            st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());

            if (L == 0 && R == 0) break;
            if (R <= 0) continue;

            lines.add(new Line(Math.max(0, L), R));
        }
        System.out.println(sol(lines));
    }

    static class Line implements Comparable<Line>{
        int s;
        int e;

        public Line(int l, int r) {
            s = l;
            e = r;
        }

        @Override
        public int compareTo(Line l) {
            return this.s - l.s;
        }
    }
}