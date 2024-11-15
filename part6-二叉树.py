#2024-11
#1、理论基础
#链式储存: 指针; 顺序储存: 数组 (如果父节点的数组下标是 i，那么它的左孩子就是 i * 2 + 1，右孩子就是 i * 2 + 2)
#定义:
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

#题2 - 递归遍历:
#递归三要素: 1.确定递归函数的参数和返回值; 2.确定终止条件; 3.确定单层递归的逻辑

#前序遍历 (leetcode 144) 中左右
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res
#中序遍历 (leetcode 94) 左中右
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res
#后序遍历 (leetcode 145) 左右中
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
        return res

#题3 - 迭代遍历
#前序: 中左右
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result
#后序: 左右中 (前序: 中左右 -> 翻转: 中右左 -> 倒序: 左右中)
class Solution:
   def postorderTraversal(self, root: TreeNode) -> List[int]:
       if not root:
           return []
       stack = [root]
       result = []
       while stack:
           node = stack.pop()
           # 中结点先处理
           result.append(node.val)
           # 左孩子先入栈
           if node.left:
               stack.append(node.left)
           # 右孩子后入栈
           if node.right:
               stack.append(node.right)
       # 将最终的数组翻转
       return result[::-1]
#中序: 左中右 (和前/后序不同的地方: 处理顺序和访问顺序不一致)
#需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result

#题4 - 统一迭代法
#前序:每次先处理的是中间节点，那么先将根节点放入栈中，然后将右孩子加入栈，再加入左孩子。
#为什么要先加入右孩子，再加入左孩子呢: 因为这样出栈的时候才是中左右的顺序。
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st= []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right: #右
                    st.append(node.right)
                if node.left: #左
                    st.append(node.left)
                st.append(node) #中
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        return result
#中序: 和前/后序不同的地方: 处理顺序和访问顺序不一致
#解决方法: 将访问的节点放入栈中，把要处理的节点也放入栈中但是要做标记 (要处理的节点放入栈之后，紧接着放入一个空指针作为标记)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right: #添加右节点（空节点不入栈）
                    st.append(node.right)
                
                st.append(node) #添加中节点
                st.append(None) #中节点访问过，但是还没有处理，加入空节点做为标记。
                
                if node.left: #添加左节点（空节点不入栈）
                    st.append(node.left)
            else: #只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop() #重新取出栈中元素
                result.append(node.val) #加入到结果集
        return result
#后序:
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                st.append(node) #中
                st.append(None)
                
                if node.right: #右
                    st.append(node.right)
                if node.left: #左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result

#题5 - 层序遍历 (leetcode 102)
#递归(层数)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        def traverse(node, level):
            if not node:
                return

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return levels
#迭代:
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result
#额外:
#107.二叉树的层次遍历II: 直接在最后反转层序遍历的结果就行
#199.二叉树的右视图: 层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了
#637.二叉树的层平均值: 每层的结果求个平均值就行
#429.N叉树的层序遍历: 层序遍历更普适的情况
#迭代
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(level)

        return result
#递归
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        result=[]
        def traversal(root,depth):
            if len(result)==depth:result.append([])
            result[depth].append(root.val)
            if root.children:
                for i in range(len(root.children)):traversal(root.children[i],depth+1)

        traversal(root,0)
        return result
#515.在每个树行中找最大值: 每层的结果求个最大值就行
#116.填充每个节点的下一个右侧节点指针 
#117.填充每个节点的下一个右侧节点指针II


#题6 - 翻转二叉树 (leetcode 226)

#题7 - 对称二叉树 (leetcode 101)

#题8 - 二叉树的最大深度 (leetcode 104)

#题9 - 二叉树的最小深度 (leetcode 111)

#题10 - 完全二叉树的节点个数 (leetcode 222)

#题11 - 平衡二叉树 (leetcode 110)

#题12 - 二叉树的所有路径 (leetcode 257)

#题13 - 左叶子之和 (leetcode 404)

#题14 - 找树左下角的值 (leetcode 513)

#题15 - 路径总和 (leetcode 112)

#题16 - 从中序与后序遍历序列构造二叉树 (leetcode 106)

#题17 - 最大二叉树 (leetcode 654)

#题18 - 合并二叉树 (leetcode 617)

#题19 - 二叉搜索树中的搜索 (leetcode 700)

#题20 - 验证二叉搜索树 (leetcode 98)

#题21 - 二叉搜索树的最小绝对差 (leetcode 530)

#题22 - 二叉搜索树中的众数 (leetcode 501)

#题23 - 二叉树的最近公共祖先 (leetcode 236)

#题24 - 二叉搜索树的最近公共祖先 (leetcode 235)

#题25 - 二叉搜索树中的插入操作 (leetcode 701)

#题26 - 删除二叉搜索树中的节点 (leetcode 450)

#题27 - 修剪二叉搜索树 (leetcode 669)

#题28 - 将有序数组转换为二叉搜索树 (leetcode 108)

#题29 - 把二叉搜索树转换为累加树 (leetcode 538)