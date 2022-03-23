import java.util.*;

public class LCA {

    public static Node findLCA(Node root, Node a, Node b) {
        if(root == null || a == null || b == null) return null;
        if (a.value == b.value) return a;
        return recursiveLCA(root, a, b);
    }

    private static Node recursiveLCA(Node currentNode, Node a, Node b) {
        if(currentNode.value == a.value || currentNode.value == b.value) return currentNode;
        if(currentNode.children == null) return null;

        List<Node> list = currentNode.children;

        int count = 0;
        List<Node> temp = new ArrayList<>();

        for(Node node : list){
            Node res = recursiveLCA(node, a, b);
            temp.add(res);
            if(res != null) {
                count++;
                if(count == 2) return currentNode;
            }
        }

        if(count == 2) return currentNode;

        for(Node t : temp){
            if(t != null) return t;
        }

        return null;
    }
}