#Brute Force: Find every path along the tree 0(n^2)
#DFS, start from the bottom track height and diameter for each node, update result

class solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)