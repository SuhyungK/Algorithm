package PGM.Lv0.구9로나눈나머지;

public class Solution {
    public int solution(String number) {
        
        return number.chars().mapToObj(Character::toString).mapToInt(Integer::parseInt).sum() % 9;
    }
}
