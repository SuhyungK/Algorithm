// 로봇 청소기

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Position {
    int x;
    int y;

    Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Position position = (Position) o;
        return x == position.x && y == position.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}

class Item {
    Position pos;
    int bitmask;

    Item(Position pos, int bitmask) {
        this.pos = pos;
        this.bitmask = bitmask;
    }
}

public class Main {
    
    static int[][] direction = new int[][] {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    static Map<Position, Integer> findDirty(char[][] arr) {
        Map<Position, Integer> positions = new HashMap<>();
        int cnt = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                if (arr[i][j] != '*') continue;
                positions.put(new Position(i, j), cnt++);
            }
        }
        return positions;
    }

    static Position findStart(char[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                if (arr[i][j] == 'o') return new Position(i, j);
            }
        }
        return null;
    }
    
    static int bfs(char[][] arr, Map<Position, Integer> positions, Position start, int h, int w) {
        int size = positions.size();
        int targetBitmask = (1 << size) - 1;
        int[][][] visited = new int[h][w][1 << size];
        Queue<Item> queue = new LinkedList<>(List.of(new Item(start, 0)));
        
        while(!queue.isEmpty()) {
            Item item = queue.poll();
            int x = item.pos.x;
            int y = item.pos.y;
            int bitmask = item.bitmask;
            int cnt = visited[x][y][bitmask];

            if (item.bitmask == targetBitmask) {
                return cnt;
            }

            for (int i = 0; i < direction.length; i++) {
                int nx = x + direction[i][0];
                int ny = y + direction[i][1];

                if (nx < 0 || ny < 0 || nx >= h || ny >= w || arr[nx][ny] == 'x') continue;
                
                if (arr[nx][ny] == '*') {
                    int nextBitmask = item.bitmask | (1 << positions.get(new Position(nx, ny)));
                    if (visited[nx][ny][nextBitmask] == 0) {
                        visited[nx][ny][nextBitmask] = cnt + 1;
                        queue.add(new Item(new Position(nx, ny), nextBitmask));
                    }
                } else if (visited[nx][ny][item.bitmask] == 0) {
                    visited[nx][ny][item.bitmask] = cnt + 1;          
                    queue.add(new Item(new Position(nx, ny), item.bitmask));
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            if (w == 0 && h == 0) break;
            
            char[][] ROOM = new char[h][w];
            for (int i = 0; i < h; i++) {
                ROOM[i] = br.readLine().toCharArray();
            }
            
            Map<Position, Integer> positions = findDirty(ROOM);
            Position startPosition = findStart(ROOM);
            System.out.println(
                bfs(ROOM, positions, startPosition, h, w)
            );
        }

    }
}
