lass Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vec = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            vec.append(node.val)
            dfs(node.right)
        
        dfs(root)

        cnt = collections.defaultdict(int)

        for val in vec:
            cnt[val] += 1

        result = []

        max_cnt = max(cnt.values())
        for val, cnt in cnt.items():
            if cnt == max_cnt:
                result.append(val)

        return result
