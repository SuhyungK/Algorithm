package PGM.Lv0.주사위게임3;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Solution {
    public int solution(int a, int b, int c, int d) {

        Map<Integer, Integer> map = new HashMap<>();

        map.put(a, map.getOrDefault(a, 0) + 1);
        map.put(b, map.getOrDefault(b, 0) + 1);
        map.put(c, map.getOrDefault(c, 0) + 1);
        map.put(d, map.getOrDefault(d, 0) + 1);

        List<Integer> list = map.values()
                                .stream()
                                .distinct()
                                .sorted()
                                .collect(Collectors.toList());

        if (list.equals(List.of(1))) {
            return Collections.min(map.keySet());
        } else if (list.equals(List.of(4))) {
            return 1111 * a;
        } else if (list.equals(List.of(2))) {
            List<Integer> keyList = map.keySet()
                                       .stream()
                                       .collect(Collectors.toList());

            int p = keyList.get(0);
            int q = keyList.get(1);
            return (p + q) * Math.abs(p - q);
        } else if (list.equals(List.of(1, 2))) {
            int result = 1;
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue()
                         .equals(2)) continue;
                result *= entry.getKey();
            }
            return result;
        } else {
            int p = 0;
            int q = 0;
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue() == 3) p = entry.getKey();
                else q = entry.getKey();
            }
            return (int) Math.pow(10 * p + q, 2);
        }
    }
}
