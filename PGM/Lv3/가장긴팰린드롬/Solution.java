package PGM.Lv3.가장긴팰린드롬;

public class Solution {

    public int solution(String s) {
        int n = s.length();

        char[] charS = s.toCharArray();
        for (int i = n; i > -1; i--) {
            for (int j = 0; j + i <= n; j++) {
                if (isPalindrome(charS, j, j + i - 1)) {
                    return i;
                }
            }
        }
        return 1;
    }

    boolean isPalindrome(char[] str, int s, int e) {
        for (int i = 0; i <= (e - s) / 2; i++) {
            if (str[s+i] != str[e-i]) return false;
        }
        return true;
    }
}
