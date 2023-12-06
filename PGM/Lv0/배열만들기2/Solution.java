package PGM.Lv0.배열만들기2;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public int[] solution(int l, int r) {
        while (true) {
            if (l % 5 == 0) break;
            l++;
        }
            
        List<Integer> answer = new ArrayList<>();
        for (int i = l; i < r; i += 5) {
            answer.add(i);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
