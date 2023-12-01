package PGM.Lv0.주사위게임3;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;


// class Solution {
//     public int solution(int a, int b, int c, int d) {
//         if (a == b && b == c && c == d) return 1111 * a;
//         else if (a == b && b == c && c != d) return (int) Math.pow(10 * a + d, 2);
//         else if (a == b && b == d && c != d) return (int) Math.pow(10 * a + c, 2);
//         else if (a == c && c == d && a != b) return (int) Math.pow(10 * a + b, 2);
//         else if (b == c && c == d && a != b) return (int) Math.pow(10 * b + a, 2);
//         else if (a == b && c == d && b != c) return (a + c) * Math.abs(a - c);
//         else if (a == d && b == c && a != b) return (a + b) * Math.abs(a - b);
//         else if (a == c && b == d && a != b) return (a + b) * Math.abs(a - b);
//         else if (a == b && c != d) return c * d;
//         else if (a == c && b != d) return b * d;
//         else if (a == d && b != c) return b * c;
//         else if (b == c && a != d) return a * d;
//         else if (b == d && a != c) return a * c;
//         else if (c == d && a != b) return a * b;
//         else return Collections.min(Arrays.asList(a, b, c, d));
//     }
// }

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
