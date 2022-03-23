import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class LCATest {

    // MAKE TREE
    private Node g = new Node('g', null);
    private Node f = new Node('f', null);
    private Node e = new Node('e', new ArrayList<>(List.of(f)));
    private Node d = new Node('d', new ArrayList<>(List.of(e,g)));
    private Node c = new Node('c', new ArrayList<>(List.of(d, e)));
    private Node b = new Node('b', new ArrayList<>(List.of(d)));
    private Node a = new Node('a', new ArrayList<>(List.of(b, c, d, e)));

    /*      TREE (* = arrow head)
              A
              |
              |\
              | \
              |  \
             /|\  \
            / | \  \
           *  |  *  \
           B  |  C  /
          / \ | /  /
         *    *   /
         G    D  /
              | /
              |/
              |
              *
              E
              |
              *
              F
     */

    @Test
    void testNull() {
        assertEquals(null, LCA.findLCA(null, null, null));
        assertEquals(null, LCA.findLCA(null, null, d));
        assertEquals(null, LCA.findLCA(null, c, null));
        assertEquals(null, LCA.findLCA(a, null, d));
        assertEquals(null, LCA.findLCA(a, c, null));
    }

    @Test
    void testSameNodes() {
        assertEquals(a, LCA.findLCA(a,a,a));
        assertEquals(b, LCA.findLCA(a,b,b));
        assertEquals(c, LCA.findLCA(a,c,c));
        assertEquals(d, LCA.findLCA(a,d,d));
        assertEquals(e, LCA.findLCA(a,e,e));
    }

    @Test
    void testNodesWithSameDirectParent() {
        assertEquals(a, LCA.findLCA(a,b,c));
        assertEquals(a, LCA.findLCA(a,d,c));
        assertEquals(a, LCA.findLCA(a,d,e));
        assertEquals(a, LCA.findLCA(a,e,c));
    }

    @Test
    void testNodesWithNoDirectCommonParent() {
        assertEquals(a, LCA.findLCA(a,b,f));
        assertEquals(a, LCA.findLCA(a,c,f));
        assertEquals(a, LCA.findLCA(a,d,f));
    }

    @Test
    void testRandomCasesWithDAG() {
        assertEquals(a, LCA.findLCA(a,b,c));
        assertEquals(a, LCA.findLCA(a,d,f));
        assertEquals(a, LCA.findLCA(a,d,b));
    }
}