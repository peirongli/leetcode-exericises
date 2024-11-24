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

                for child in node.children:#推广: 不止有左右child
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
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return []
            
        queue = deque([root])
        while queue:

            n = len(queue)
            prev = None
            for i in range(n):
                curr = queue.popleft()
                if prev:
                    prev.next = curr
                prev = curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root
#117.填充每个节点的下一个右侧节点指针II: 同上


#题6 - 翻转二叉树 (leetcode 226)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                #if curr.left and curr.right: 。注意这个判断条件不需要加, 不要多此一举
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root

#题7 - 对称二叉树 (leetcode 101)
#注意要比较的不是左右节点, 所以要同时遍历左右子树来比较
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode:
                continue
            
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True

#题8 - 二叉树的最大深度 (leetcode 104)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        result = 0

        while queue:
            result += 1
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result

#题9 - 二叉树的最小深度 (leetcode 111)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        result = 0
        while queue:
            n = len(queue)
            result += 1
            for i in range(n):         
                curr = queue.popleft()
                if (not curr.left) and (not curr.right):
                    return result
                else:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return result

#题10 - 完全二叉树的节点个数 (leetcode 222)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        result = 1
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    result += 1
                if curr.right:
                    queue.append(curr.right)
                    result += 1
        return result

#题11 - 平衡二叉树 (leetcode 110)
#本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1
#暴力法(通过225/228个测试用例):
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = collections.deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    if not curr.right:
                        if curr.left.left or curr.left.right:
                            return False
                    if curr.right and (not curr.right.left) and (not curr.right.right):
                        if curr.left.left:
                            if curr.left.left.left or curr.left.left.right:
                                return False
                        if curr.left.right:
                            if curr.left.right.left or curr.left.right.right:
                                return False
                if curr.right:
                    queue.append(curr.right)
                    if not curr.left:
                        if curr.right.left or curr.right.right:
                            return False
                    if curr.left and (not curr.left.left) and (not curr.left.right):
                        if curr.right.left:
                            if curr.right.left.left or curr.right.left.right:
                                return False
                        if curr.right.right:
                            if curr.right.right.left or curr.right.right.right:
                                return False
        return True

#题12 - 二叉树的所有路径 (leetcode 257)
#用前序遍历, 要回溯
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        stack = [root]
        path_stack = [str(root.val)]
        result = []
        while stack:
            curr = stack.pop()
            path = path_stack.pop()
            if (not curr.left) and (not curr.right):
                result.append(path)
            if curr.right:
                stack.append(curr.right)
                path_stack.append(path + '->' + str(curr.right.val))
            if curr.left:
                stack.append(curr.left)
                path_stack.append(path + '->' + str(curr.left.val))
        return result

#题13 - 左叶子之和 (leetcode 404)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        sum = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    if (not curr.left.left) and (not curr.left.right):
                        sum += curr.left.val
                if curr.right:
                    queue.append(curr.right)
        return sum

#题14 - 找树左下角的值 (leetcode 513)
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
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
        left_most = result[-1][0]
        return left_most

#题15 - 路径总和 (leetcode 112)
#无脑版: 照搬lc257所有路径, 在它的基础上加上判断的处理就行 (可能在lc113用这个方法更好, 因为它要找所有符合的路径)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [root]
        path_stack = [str(root.val)]
        result = []
        while stack:
            curr = stack.pop()
            path = path_stack.pop()
            if (not curr.left) and (not curr.right):
                result.append(path)
            if curr.right:
                stack.append(curr.right)
                path_stack.append(path + '->' + str(curr.right.val))
            if curr.left:
                stack.append(curr.left)
                path_stack.append(path + '->' + str(curr.left.val))
        
        for path in result:
            vals = path.split('->')
            sum = 0
            for val in vals:
                sum += int(val)
            if sum == targetSum:
                return True
        return False
#正常迭代
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        # 栈里放的是pair<节点指针，路径数值>
        st = [(root, root.val)]
        while st:
            node, path_sum = st.pop()
            # 如果该节点是叶子节点了，同时该节点的路径数值等于sum，那么就返回true
            if not node.left and not node.right and path_sum == sum:
                return True
            if node.right:
                st.append((node.right, path_sum + node.right.val))
            if node.left:
                st.append((node.left, path_sum + node.left.val))
        return False

#题16 - 从中序与后序遍历序列构造二叉树 (leetcode 106)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_idx = inorder.index(root_val)

        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1:]

        postorder_left = postorder[:root_idx]
        postorder_right = postorder[root_idx:-1]

        #递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        return root
#额外: 从前序与中序遍历序列构造二叉树 (leetcode 105)
#注意: 前序和后序不能唯一确定一棵二叉树，因为没有中序遍历无法确定左右部分，也就是无法分割
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)

        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1:]

        preorder_left = preorder[1:root_idx + 1]
        preorder_right = preorder[root_idx + 1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

#题17 - 最大二叉树 (leetcode 654)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root_val = max(nums)
        root_idx = nums.index(root_val)
        root = TreeNode(root_val)

        left_tree = nums[:root_idx]
        right_tree = nums[root_idx + 1:]

        root.left = self.constructMaximumBinaryTree(left_tree)
        root.right = self.constructMaximumBinaryTree(right_tree)

        return root

#题18 - 合并二叉树 (leetcode 617)
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        
        root_val = root1.val + root2.val
        root = TreeNode(root_val)
        
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root
#改进: 可以重复使用题目给出的节点而不是创建新的节点来节省时间, 空间

#题19 - 二叉搜索树中的搜索 (leetcode 700)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.val == val:
                    return curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return None

#题20 - 验证二叉搜索树 (leetcode 98)
#二叉搜索树是一个有序树:
#若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
#若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
#它的左、右子树也分别为二叉搜索树
#初版: 通过77/85个测试用例. 误区: 没有考虑左(右)子树的所有节点都必须小(大)于当前节点
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = collections.deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    if curr.left.val >= curr.val:
                        return False
                if curr.right:
                    queue.append(curr.right)
                    if curr.right.val <= curr.val:
                        return False
        return True
#比较巧妙的方法: 中序遍历下，输出的二叉搜索树节点的数值是有序序列。利用这个特性，验证二叉搜索树，就等于判断一个序列是否递增
class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None  # 记录前一个节点
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left  # 左
            else:
                cur = stack.pop()  # 中
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur  # 保存前一个访问的结点
                cur = cur.right  # 右
        return True

#题21 - 二叉搜索树的最小绝对差 (leetcode 530)
#还是利用bst中序遍历结果是有序数组的特性做
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        stack = []
        result = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        diff = result[1] - result[0]
        for i in range(2, len(result)):
            temp = result[i] - result[i-1]
            if temp < diff:
                diff = temp
        return diff

#题22 - 二叉搜索树中的众数 (leetcode 501)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        stack = []
        result = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        #找重数的这一步还有待优化
        freq = {}
        for i in range(len(result)):
            if result[i] not in freq.keys():
                freq.update({result[i]: 1})
            else:
                freq[result[i]] += 1
        max_value = max(freq.values())
        max_keys = [key for key, value in freq.items() if value == max_value]
        return max_keys

#题23 - 二叉树的最近公共祖先 (leetcode 236)
#本题用迭代不合适, 用递归
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == q or root == p or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None:
            return right
        return left

#题24 - 二叉搜索树的最近公共祖先 (leetcode 235)
#因为bst的特性, 从上向下遍历，第一次遇到curr节点的数值在[p, q]区间中，那么curr就是p和q的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if (curr.val >= p.val and curr.val <= q.val) or (curr.val >= q.val and curr.val <= p.val):
                    return curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return None
#精简版:
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None

#题25 - 二叉搜索树中的插入操作 (leetcode 701)
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        elif root.val > val:
            if not root.left:
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        elif root.val < val:
            if not root.right:
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        return root

#题26 - 删除二叉搜索树中的节点 (leetcode 450)
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = TreeNode(key)
        if not root:
            return None
        elif root.val == key:
            if (not root.left) and (not root.right):
                root = None
            elif root.left and (not root.right):
                root = root.left
            elif (not root.left) and root.right:
                root = root.right
            elif root.left and root.right:#最复杂的情况: 将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
                curr = root.right
                while curr.left is not None:
                    curr = curr.left
                curr.left = root.left
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

#题27 - 修剪二叉搜索树 (leetcode 669)
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val < low:
            root = root.right
            return self.trimBST(root, low, high)
        elif root.val > high:
            root = root.left
            return self.trimBST(root, low, high)
        else: #low < root.val < high
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root

#题28 - 将有序数组转换为二叉搜索树 (leetcode 108)
#在题17 - 最大二叉树 (leetcode 654)的基础上稍做修改即可
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        mid = n//2
        root_val = nums[mid]
        root = TreeNode(root_val)

        left_tree = nums[:mid]
        right_tree = nums[mid + 1:]

        root.left = self.sortedArrayToBST(left_tree)
        root.right = self.sortedArrayToBST(right_tree)

        return root

#题29 - 把二叉搜索树转换为累加树 (leetcode 538)
#在中序遍历的基础上做一点修改即可
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = []
        total = 0
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                total += curr.val
                curr.val = total
                curr = curr.left
        return root
