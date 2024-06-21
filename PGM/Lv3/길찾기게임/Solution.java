package PGM.Lv3.길찾기게임;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        s.solution(new int[][] {{5,3},{11,5},{13,3},{3,5},{6,1},{1,3},{8,6},{7,2},{2,2}});
    }

    public int[][] solution(int[][] nodeinfo) {

        List<Node> tree = new ArrayList<>();
        for (int i = 0; i < nodeinfo.length; i++) {
            tree.add(new Node(nodeinfo[i][0], nodeinfo[i][1], i+1));
        }
        Collections.sort(tree);

        int[][] answer = new int[2][nodeinfo.length];
        answer[0] = preOrder(tree, new ArrayList<>()).stream().mapToInt(i -> i).toArray();
        answer[1] = postOrder(tree, new ArrayList<>()).stream().mapToInt(i -> i).toArray();
        return answer;
    }

    public List<Integer> preOrder(List<Node> nodes, List<Integer> orders) {
        if (nodes.size() == 0) return orders;
        Node cur = nodes.get(0);
        orders.add(cur.num);

        List<Node> leftChild = new ArrayList<>();
        List<Node> rightChild = new ArrayList<>();
        for (int i = 1; i < nodes.size(); i++) {
            Node child = nodes.get(i);
            if (cur.x > child.x) leftChild.add(child);
            else rightChild.add(child);
        }

        orders = preOrder(leftChild, orders);
        orders = preOrder(rightChild, orders);

        return orders;
    }

    public List<Integer> postOrder(List<Node> nodes, List<Integer> orders) {
        if (nodes.size() == 0) return orders;
        Node cur = nodes.get(0);

        List<Node> leftChild = new ArrayList<>();
        List<Node> rightChild = new ArrayList<>();
        for (int i = 1; i < nodes.size(); i++) {
            Node child = nodes.get(i);
            if (cur.x > child.x) leftChild.add(child);
            else rightChild.add(child);
        }
        orders = postOrder(leftChild, orders);
        orders = postOrder(rightChild, orders);

        orders.add(cur.num);
        return orders;
    }

    class Node implements Comparable<Node>{
        int x;
        int y;
        int num;

        Node(int x, int y, int num) {
            this.x = x;
            this.y = y;
            this.num = num;
        }

        @Override
        public int compareTo(Node o) {
            if (this.y == o.y) return this.x - o.x;
            return o.y - this.y;
        }
    }
}
