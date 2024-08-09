class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self is None:
            return None
        val_str = f"value {self.val}, "
        left_str = "left is None, " if self.left is None else f"left val {self.left.val}, "
        right_str = "right is None" if self.right is None else f"right val {self.right.val}"

        return val_str + left_str + right_str


    def preorder(self):
        if self is not None:
            print(self)
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.val)
            if self.right is not None:
                self.right.inorder()

    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.val)


class Solution(object):
    def isValidBSD(self, root):
        pass

    def arrayToTree(self, root, index=0):
        tree = TreeNode()
        if index < len(root):
            tree.val = root[index]
            if root[index] == 'null':
                print("met null")
                return None, index + 1
        else:
            return None, len(root)

        leftSub, rightBeg = self.arrayToTree(root, index + 1)
        print(leftSub, "right beg", rightBeg)
        rightSub, rightEnd = self.arrayToTree(root, rightBeg)
        tree.left = leftSub
        tree.right = rightSub
        return tree, rightEnd


if __name__ == '__main__':
    sol = Solution()
    tree, ind = sol.arrayToTree(root=[5,1,4,"null","null",3,6])
    # tree.preorder()
    # tree.postorder()
    # tree.inorder()
