package PGM.Lv1;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class 가장많이받은선물 {
        public static void main(String[] args) {
        가장많이받은선물 it = new 가장많이받은선물();
        System.out.println(it.solution(
                new String[]{"muzi", "ryan", "frodo", "neo"},
                new String[]{"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"}
        ));
        System.out.println(it.solution(
                new String[]{"joy", "brad", "alessandro", "conan", "david"},
                new String[]{"alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"}
        ));
    }

    public int solution(String[] friends, String[] gifts) {
        int N = friends.length;
        Map<String, Integer> friendsMap = new HashMap<>();
        for (int i = 0; i < N; i++) {
            friendsMap.put(friends[i], i);
        }

        int[][] giftTable = new int[N][N]; // 행 : 준 사람 / 열 : 받은 사람
        int[] giftIndex = new int[N];

        for (String gift : gifts) {
            String[] fromTo = gift.split(" ");
            int from = friendsMap.get(fromTo[0]);
            int to = friendsMap.get(fromTo[1]);
            giftTable[from][to] += 1;
            giftIndex[from] += 1;
            giftIndex[to] -= 1;
        }

        int A;
        int B;
        int[] answer = new int[N];
        for (int i = 0; i < N - 1; i++) {
            A = friendsMap.get(friends[i]);
            for (int j = i + 1; j < N; j++) {
                B = friendsMap.get(friends[j]);

                if (giftTable[A][B] > giftTable[B][A]) {
                    // A가 B한테 선물 더 많이 줌
                    answer[A] += 1;
                }
                else if (giftTable[A][B] < giftTable[B][A]) {
                    answer[B] += 1;
                } else if (giftIndex[A] > giftIndex[B]) {
                    answer[A] += 1;
                } else if (giftIndex[A] < giftIndex[B]) {
                    answer[B] += 1;
                }
            }
        }

        return Arrays.stream(answer)
                     .max()
                     .getAsInt();
    }
}
