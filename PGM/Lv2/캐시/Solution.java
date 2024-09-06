package PGM.Lv2.캐시;
import java.util.*;

public class Solution {
    static final int CACHE_HIT = 1;
    static final int CACHE_MISS = 5;

    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) {
            return CACHE_MISS * cities.length;
        }

        List<String> cache = new LinkedList<>();

        int answer = 0;
        for (String city: cities) {
            int idx = cache.indexOf(city.toLowerCase());
            if (idx == -1) {
                // 캐시에 없는 경우
                if (cache.size() == cacheSize) {
                    cache.remove(0);
                }
                cache.add(city.toLowerCase());
                answer += CACHE_MISS;
            } else {
                cache.remove(idx);
                cache.add(city.toLowerCase());
                answer += CACHE_HIT;
            }
        }
        return answer;
    }
}