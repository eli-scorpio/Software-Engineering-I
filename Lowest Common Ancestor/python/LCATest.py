# Author: Eligijus Skersonas

import unittest
from LCA import LCA
from Node import Node

# Test LCA
class TestLCA(unittest.TestCase):
    # Make Tree
    root = Node(1);
    root.left = Node(2);
    root.right = Node(3);
    root.left.left = Node(4);
    root.left.right = Node(5);
    root.right.left = Node(6);
    root.right.right = Node(7);
    lca = LCA();

    # Test LCA root is null
    def test_NullRoot(self):
        self.assertEqual(self.lca.lowest_common_ancestor(None,self.root.left,self.root.right), None)

    # Test LCA where all parameters are null
    def test_AllNull(self):
        self.assertEqual(self.lca.lowest_common_ancestor(None,None,None), None)

    # Test LCA where one person is not in the tree
    def test_PersonNotInTree(self):
        self.assertEqual(self.lca.lowest_common_ancestor(self.root,Node(10),self.root.left), None)

    # Test LCA where both persons are not in the tree
    def test_BothPersonsNotInTree(self):
        self.assertEqual(self.lca.lowest_common_ancestor(self.root,Node(10),Node(11)), None)

    # Test LCA where the tree is a single node
    def test_SingleNodeTree(self):
        root = Node(1);
        self.assertEqual(self.lca.lowest_common_ancestor(root,root,root).val,root.val)

    # Test LCA where person1 and person2 is left of the root
    def test_LCA_LeftOfRoot(self):
        person1 = self.root.left.left;
        person2 = self.root.left.right;
        self.assertEqual(self.lca.lowest_common_ancestor(self.root,person1,person2).val,2)
    
    # Test LCA where person1 and person2 is right of the root
    def test_LCA_RightOfRoot(self):
        person1 = self.root.right.left;
        person2 = self.root.right.right;
        self.assertEqual(self.lca.lowest_common_ancestor(self.root,person1,person2).val,3)

    # Test LCA where person1 is parent of person2
    def test_LCA_ParentAndChild(self):
        person1 = self.root.left;
        person2 = self.root.left.right;
        self.assertEqual(self.lca.lowest_common_ancestor(self.root,person1,person2).val,2)

    # Test LCA where person1 is left of the root and person2 is right of the root
    def test_LCA_1Right_1Left(self):
        person1 = self.root.left.left;
        person2 = self.root.right.right;
        self.assertEqual(self.lca.lowest_common_ancestor(self.root, person1, person2).val, 1)
    


if __name__ == '__main__':
    unittest.main()