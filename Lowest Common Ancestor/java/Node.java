import java.util.*;
class Node{
    char value;
    List<Node> children;

    Node (char value, List<Node> children){
        this.value = value;
        this.children = children;
    }
}