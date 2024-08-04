package PGM.Lv2.오픈채팅방;

import java.util.*;

public class Solution {
    static Map<String, String> users = new HashMap<>(); // 유저 테이블
    static List<Chat> chatRecord = new ArrayList<>(); // 채팅방 기록

    public String[] solution(String[] record) {
        String[] parseData;
        for (String row : record) {
            parseData = row.split(" ");

            if (parseData[0].equals("Enter")) {
                enter(parseData[1], parseData[2]);
            } else if (parseData[0].equals("Leave")) {
                leave(parseData[1]);
            } else if (parseData[0].equals("Change")) {
                change(parseData[1], parseData[2]);
            }

        }

        String[] result = new String[chatRecord.size()];
        Chat chat;
        for (int i = 0; i < result.length; i++) {
            chat = chatRecord.get(i);
            if (chat.isEnter) {
                result[i] = users.get(chat.userId) + "님이 들어왔습니다.";
            } else {
                result[i] = users.get(chat.userId) + "님이 나갔습니다.";
            }
        }
        return result;
    }

    void enter(String userId, String nickname) {
        // 유저 입장시
        users.put(userId, nickname);
        chatRecord.add(new Chat(userId, true));
    }

    void leave(String userId) {
        // 유저 퇴장시
        chatRecord.add(new Chat(userId, false));
    }

    void change(String userId, String newNickname) {
        // 닉네임 변경
        users.put(userId, newNickname);
    }

    class Chat {
        public String userId;
        public boolean isEnter;

        Chat(String userId, boolean isEnter) {
            this.userId = userId;
            this.isEnter = isEnter;
        }
    }
}