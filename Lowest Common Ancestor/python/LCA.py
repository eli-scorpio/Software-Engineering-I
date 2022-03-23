#Author: Eligijus Skersonas

from Node import Node

class LCA:

    def lowest_common_ancestor(self, root, person1, person2):
        # if any parameter is null return null
        if((root is None) or (person1 is None) or (person2 is None)):
            return None;
        # if either person is not in the tree return null
        if((self.in_tree(root, person1) is False) or (self.in_tree(root, person2) is False)):
            return None;

        return self.recursive_lca(root, person1, person2);

    def recursive_lca(self, root, person1, person2):
        if root is None:
            return None;
        if (root.val is person1.val) or (root.val is person2.val):
            return root;
        
        left_lca = self.recursive_lca(root.left, person1, person2);
        right_lca = self.recursive_lca(root.right, person1, person2);

        # if a person was in the left and a person was in the right return current Node
        if (left_lca is not None) and (right_lca is not None):
            return root;
        # if person/lca was in the left return the left_lca otherwise return the right_lca
        elif left_lca is not None:
            return left_lca;
        else:
            return right_lca;

    # method to check if person is in given tree
    def in_tree(self, root, person):
        if(root == None):
            return False;
        elif(root.val == person.val):
            return True;
        
        in_left = self.in_tree(root.left, person);
        in_right = self.in_tree(root.right, person);

        return in_left or in_right;

        