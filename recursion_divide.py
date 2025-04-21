def my_pow(x: float, n: int) -> float:
    """
    求实现 pow(x, n)，即计算 x 的 n 次幂函数(LeetCode.50)
    快速幂算法（递归）
    :param x:
    :param n:
    :return:
    """

    def fast_pow(y, m):
        if m == 0:
            return 1.0
        half = fast_pow(y, m // 2)
        if m % 2 == 0:
            return half * half
        else:
            return half * half * y

    if n < 0:
        x = 1 / x
        n = -n
    return fast_pow(x, n)


def my_pow_loop(x: float, n: int) -> float:
    """
    快速幂算法（迭代）
    :param x:
    :param n:
    :return:
    """
    if n < 0:
        x = 1 / x
        n = -n

    res = 1
    current_product = x
    while n > 0:
        if n % 2 == 1:  # 如果是奇数, 少乘一个x
            res *= current_product
        current_product *= current_product
        n = n // 2
    return res


def majority_element(nums: list[int]) -> int:
    """
    求找出数组中出现次数超过 ⌊n//2⌋ 的元素（多数元素） n为数组长度
    哈希法计数
    :param nums:
    :return:
    """
    count = {}
    for num in nums:
        # 统计每个数字出现的次数
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:  # 向下取整
            return num


def majority_element_sort(nums: list[int]) -> int:
    """
    排序法
    :param nums:
    :return:
    """
    nums.sort()
    return nums[len(nums) // 2]


def majority_element_bm(nums: list[int]) -> int:
    """
    Boyer-Moore 投票算法
    :param nums:
    :return:
    """
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


def generate_parenthesis(n: int) -> list[str]:
    """
    生成有效的括号组合(leetcode.22)
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    """

    def _gen_parenthesis(left: int, right: int, m: int, res: str):
        # 如果左右括号的数量全部用完，说明全部组合完毕
        if left == m and right == m:
            result.append(res)  # 可以写入结果集
            return
        if left < n:  # 说明左括号没用完，继续用左括号
            _gen_parenthesis(left + 1, right, m, res + "(")
        if right < left and right < n:  # 左右括号没有匹配完毕，继续使用右括号
            _gen_parenthesis(left, right + 1, m, res + ")")

    result = []
    _gen_parenthesis(0, 0, n, "")
    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_through_bt_loop(root: TreeNode) -> list[list[int]]:
    """
    层序遍历二叉树(leetcode.102)
    迭代法
    """
    if not root:
        return []
    from collections import deque
    # 初始化我们的结果和队列
    result, queue = [], deque
    # 首先 root进入队列
    queue.append(root)
    while queue:
        # 定义当前层级的val和当前层级的大小
        current_level_val_list, level_size = [], len(queue)
        for _ in range(level_size):
            curr_node = queue.popleft()
            current_level_val_list.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.append(current_level_val_list)
    return result


def level_through_bt_recursion(root: TreeNode) -> list[list[int]]:
    """
    递归法
    """

    def dfs(node: TreeNode, level: int):
        if not node:
            return
        if len(result) < level + 1:
            result.append([])
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    if not root:
        return []
    result = []
    dfs(root, 0)
    return result


def solve_n_queen(n: int) -> list[list[str]]:
    """
    求解n皇后问题，"Q"表示皇后，"."表示空格(leetcode.51)
    """

    # 结果数组
    solutions = []
    # 初始化棋盘和辅助集合
    cols = set()  # 记录被占用的列
    diag = set()  # 记录被占用的主对角线
    anti_diag = set()  # 记录被占用的主副对角线
    # 初始化棋盘, '.'为空位， 'Q'表示皇后
    board = [["." for _ in range(n)] for _ in range(n)]

    def backtrack(r: int):
        # 如果已经放置过N个皇后（遍历完所有的行）， 则找到一种解决方案
        if r == n:
            # 格式化当前棋盘状态
            formatted_board = ["".join(row) for row in board]
            solutions.append(formatted_board)
            return
        # 尝试在当前行每一列放置皇后
        for c in range(n):
            # 检查当前位置是否安全（不在被占用的列、主副对角线上）
            if c not in cols and (r + c) not in diag and (r - c) not in anti_diag:
                # 放置皇后
                cols.add(c)
                diag.add(r + c)
                anti_diag.add(r - c)
                board[r][c] = 'Q'
                # 递归调用， 处理下一行
                backtrack(r + 1)

                # 回溯： 移除皇后，尝试其他的列
                cols.remove(c)
                diag.remove(r + c)
                anti_diag.remove(r - c)
                board[r][c] = '.'

    # 从第一行 (索引0)开始回溯
    backtrack(0)
    return solutions


def total_n_queens(n: int) -> int:
    """
    求n皇后解的个数(leetcode.51)
    """
    count = 0  # 记录解决方案的总数

    # 使用集合记录已占用的位置
    cols = set()  # 记录被占用的列
    diag = set()  # 记录被占用的主对角线 (r + c)
    # 修正注释
    anti_diag = set()  # 记录被占用的副对角线 (r - c)

    def backtrack(row: int):
        """
        row: 当前处理的行数
        """
        nonlocal count  # 声明使用外部作用域的 count 变量

        # 如果已经放置了N个皇后（遍历完所有行），则找到一个解决方案
        if row == n:
            count += 1  # 直接修改外部的 count 变量
            return  # 找到解后结束当前路径的回溯

        # 尝试在当前行的每一列放置皇后
        for c in range(n):
            # 检查当前位置 (row, c) 是否安全
            if c not in cols and (row + c) not in diag and (row - c) not in anti_diag:
                # 放置皇后，更新占用的集合
                cols.add(c)
                diag.add(row + c)
                anti_diag.add(row - c)

                # 递归调用，处理下一行
                # 这里不需要接收返回值，因为 count 是通过 nonlocal 直接修改的
                backtrack(row + 1)

                # 回溯：移除皇后，恢复状态，尝试当前行的其他列
                cols.remove(c)
                diag.remove(row + c)
                anti_diag.remove(row - c)

    # 从第一行（索引0）开始启动回溯过程
    backtrack(0)
    return count  # 返回最终的总数


# 示例用法
# print(total_n_queens(4)) # 输出 2
# print(total_n_queens(8)) # 输出 92

def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    有效数独(leetcode.36)
    """
    rows = [set() for _ in range(9)]  # 记录每一行出现的数字
    cols = [set() for _ in range(9)]  # 记录每一列出现的数字
    boxes = [set() for _ in range(9)]  # 记录每一个3*3子格出现的数字

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            # 计算当前单元格所属的 3*3 子格的索引
            box_index = (r // 3) * 3 + (c // 3)
            # 检查当前数字是否已在行、列或子格中出现过
            if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                return False  # 发现重复，数独无效
            # 将当前数字添加到对应的行、列和子格记录中
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_index].add(num)
    # 遍历整个棋盘都没发现重复，数独有效
    return True


def solve_sudoku(board: list[list[str]]) -> None:
    """
    这道题目要求填充一个 9x9 的数独棋盘，使得其成为一个有效的（且完整填充的）数独。(LeetCode.37)
    我们可以使用回溯算法来解决这个问题。
    回溯算法的基本思路是：
    1.找到棋盘中的一个空单元格（'.'）。
    2.尝试在当前空单元格中填入数字 1-9。
    3.对于每一个尝试填入的数字，检查其是否符合数独规则（与当前行、列和 3x3 子格中的其他数字不冲突）。
    4.如果填入的数字有效，则递归调用回溯函数，去解决下一个空单元格。
    5.如果在当前单元格填入某个数字后，后续的递归调用成功找到了一个完整的解，
      则说明当前数字是正确的，整个问题得解，返回 True。
    6.如果当前单元格尝试了数字 1-9 后，都没有找到一个有效的解（即后续的递归调用都失败了），
      则说明当前单元格的假设是错误的，需要进行回溯。将当前单元格重新置为空（'.'），并返回 False，
      以便上层调用可以尝试其他可能性。
    7.如果整个棋盘都没有空单元格了，说明已经找到了一个完整的解，返回 True。
    由于我们需要修改原始棋盘（原地解），所以回溯时需要撤销之前的修改。
    """
    # 使用集合预处理已有的数字，提高查询效率
    rows = [set() for _ in range(9)]  # 行
    cols = [set() for _ in range(9)]  # 列
    boxes = [set() for _ in range(9)]  # 3 * 3
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != '.':
                rows[r].add(num)
                cols[c].add(num)
                box_index = (r // 3) * 3 + (c // 3)
                boxes[box_index].add(num)

    def is_valid(_r, _c, _num):
        """检查board[_r][_c]放置的数字num是否有效"""
        box_idx = (_r // 3) * 3 + (_c // 3)
        return _num not in rows[_r] and _num not in cols[_c] and _num not in boxes[box_idx]

    def place_number(_r, _c, _num):
        """
        在boxes[_r][_c]中放置数字num，并更新对应的集合
        """
        rows[_r].add(_num)
        cols[_c].add(_num)
        box_idx = (_r // 3) * 3 + (_c // 3)
        boxes[box_idx].add(_num)
        board[_r][_c] = _num

    def remove_number(_r, _c, _num):
        """
        从board[_r][_c]移除不符合条件的数字，并更新集合（回溯时用）
        """
        rows[_r].remove(_num)
        cols[_c].remove(_num)
        box_idx = (_r // 3) * 3 + (_c // 3)
        boxes[box_idx].remove(_num)
        board[_r][_c] = '.'

    def find_empty(_board):
        """找到棋盘中第一个空单元格 '.'"""
        for r in range(9):
            for c in range(9):
                if _board[r][c] == '.':
                    return r, c
        return -1, -1  # 没有空的单元格

    def backtrack():
        _r, _c = find_empty(board)
        # 如果没有找到空单元格，说明数组全部解开了
        if _r == -1:
            return True
        for _num in "123456789":
            # 如果数字满足条件, 放入数字
            if is_valid(_r, _c, _num):
                place_number(_r, _c, _num)
                # 递归调用，尝试解决剩余部分
                if backtrack():
                    return True  # 如果递归调用返回True，表示找到一个完整的解
                # 如果递归调用返回False 说明数字不满足条件，要回溯,删除已经填入的数字
                remove_number(_r, _c, _num)
        # 如果所有的数字都没有扎到解，返回False
        return False

    # 从第一个空单元格开始
    backtrack()


# 如何在本地测试并看到结果：
# 创建一个数独盘面（需要保证是有效数独，否则可能无解）
# 示例输入 (来自 LeetCode 题目描述)
board_to_solve = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solve_sudoku(board_to_solve)
# 打印解好的数独盘面
print("解好的数独盘面:")
for row in board_to_solve:
    print(" ".join(row))


class Trie:
    """
    实现一个 Trie（前缀树）(LeetCode.208)
    Trie 是一种树形数据结构，用于存储字符串集合。它的主要优势在于可以高效地进行前缀匹配。一个 Trie 的结构通常是这样的：
    * 根节点不存储任何字符。
    * 每个节点存储一个字符。
    * 从根节点到某个节点的路径上的字符组合起来表示一个字符串的前缀。
    * 某些节点会被标记为单词的结尾，表示从根节点到该节点的路径形成了一个完整的单词。

    你需要实现 `Trie` 类，并包含以下三个方法：

    1.  `insert(word)`: 向 Trie 中插入一个单词。
    2.  `search(word)`: 判断 Trie 中是否存在完整的单词 `word`。
    3.  `startsWith(prefix)`: 判断 Trie 中是否存在以 `prefix` 为前缀的单词。

    我们可以使用嵌套字典或者自定义节点类来实现 Trie。使用嵌套字典的方式比较简洁直观。每个节点（字典）的键是子节点的字符，值是对应的子节点（另一个字典）。
    下面是使用嵌套字典实现的 Python 代码：

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用一个字典来表示 Trie 的节点
        # 键是字符，值是对应的子节点 (另一个字典)
        # '_end_': 一个特殊标记，表示当前节点是某个单词的结尾
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            # 如果当前字符不在当前节点的子节点中，则创建一个新的子节点
            if char not in node:
                node[char] = {}
            # 移动到下一个节点 (子节点)
            node = node[char]
        # 在单词的最后一个字符对应的节点处做一个标记，表示这里是一个完整的单词的结尾
        node['_end_'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            # 如果当前字符不在当前节点的子节点中，说明该单词不存在于 Trie 中
            if char not in node:
                return False
            # 移动到下一个节点
            node = node[char]
        # 遍历完所有字符后，检查当前节点是否有单词结尾标记 '_end_'
        # 只有有标记才表示这是一个完整的单词
        return '_end_' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            # 如果当前字符不在当前节点的子节点中，说明没有单词以该前缀开头
            if char not in node:
                return False
            # 移动到下一个节点
            node = node[char]
        # 如果能顺利遍历完所有前缀字符，说明至少有一个单词以该前缀开头
        # 不需要在意是否有 '_end_' 标记，因为只要路径存在即可
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""
解释:

* `__init__`: 初始化时，创建一个空的字典 `self.root` 作为 Trie 的根节点。
* `insert(word)`: 遍历单词的每个字符。从根节点开始，对于每个字符，如果当前节点没有对应的子节点，就创建一个新的空字典作为子节点，并将当前节点移动到这个子节点。遍历完单词后，在最后一个字符对应的节点字典中添加一个特殊键值对 `'_end_': True`，用来标记这个节点是单词的结束。
* `search(word)`: 遍历单词的每个字符。如果发现任何一个字符在当前节点的子节点中不存在，说明整个单词不存在，返回 `False`。如果能顺利遍历完所有字符，最后检查当前节点是否有 `'_end_'` 标记。只有存在标记，才表示 `word` 是一个完整的被插入过的单词。
* `startsWith(prefix)`: 遍历前缀的每个字符。如果发现任何一个字符在当前节点的子节点中不存在，说明没有单词以该前缀开头，返回 `False`。如果能顺利遍历完所有前缀字符，说明这条前缀路径是存在的，至少有一个单词以它开头，返回 `True`。

这种实现方式简单直观，利用字典来表示节点之间的链接关系。键是字符，值是指向下一个节点的引用。特殊键 `'_end_'` 用于区分某个前缀本身是否构成一个完整的单词。
"""


class TrieNode:
    """
    好的，我们来使用 `list` 来实现 Trie。
    使用 `list` 来表示子节点通常意味着我们知道所有可能的字符范围。对于 LeetCode 208 题，输入的单词只包含小写英文字母 `a-z`，所以每个节点最多可以有 26 个子节点。
    我们可以用一个长度为 26 的列表，列表的索引对应字符的顺序（例如，索引 0 对应 'a'，索引 1 对应 'b'，...，索引 25 对应 'z'）。列表的每个元素存储指向对应子节点的引用。
    这种实现方式通常比使用字典在查找速度上略快（直接通过索引访问是 O(1)），但在空间上可能会占用更多固定空间，即使某些字符的子节点为空（列表元素为 `None`）。
    首先，我们需要定义一个节点类来表示 Trie 中的每一个节点：
    """

    def __init__(self):
        # 使用一个长度为 26 的列表来存储子节点
        # children[0] 对应字符 'a' 的子节点
        # children[1] 对应字符 'b' 的子节点
        # ...
        # children[25] 对应字符 'z' 的子节点
        # 如果某个位置为 None，表示没有对应的子节点
        self.children = [None] * 26

        # 标志位，表示从根节点到当前节点形成的路径是否构成一个完整的单词
        self.is_end_of_word = False


class TrieList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Trie 的根节点是一个 TrieNode 实例
        self.root = TrieNode()

    def _char_to_index(self, char: str) -> int:
        """
        helper 方法：将小写英文字母映射到 0-25 的索引
        """
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root  # 从根节点开始
        for char in word:
            index = self._char_to_index(char)  # 获取当前字符对应的索引

            # 如果当前节点的 children 列表中，该索引位置没有子节点，则创建一个新的 TrieNode
            if node.children[index] is None:
                node.children[index] = TrieNode()

            # 移动到下一个节点 (子节点)
            node = node.children[index]

        # 遍历完单词的所有字符后，将当前节点标记为单词的结尾
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root  # 从根节点开始
        for char in word:
            index = self._char_to_index(char)  # 获取当前字符对应的索引

            # 如果当前节点的 children 列表中，该索引位置为 None，
            # 说明沿着这个路径找不到对应的字符，该单词不存在
            if node.children[index] is None:
                return False

            # 移动到下一个节点
            node = node.children[index]

        # 遍历完所有字符后，检查当前节点是否是某个单词的结尾
        # 只有是结尾才表示找到了完整的单词
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root  # 从根节点开始
        for char in prefix:
            index = self._char_to_index(char)  # 获取当前字符对应的索引

            # 如果当前节点的 children 列表中，该索引位置为 None，
            # 说明沿着这个路径找不到对应的字符，没有单词以该前缀开头
            if node.children[index] is None:
                return False

            # 移动到下一个节点
            node = node.children[index]

        # 如果能顺利遍历完所有前缀字符，说明这条前缀路径存在
        # 即使当前节点不是单词结尾，也表示有单词以该前缀开头
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""

**解释:**

1.  **`TrieNode` 类:** 定义了 Trie 中的一个节点。它包含一个长度为 26 的 `children` 列表，用于存放指向子节点的引用；一个布尔型的 `is_end_of_word` 标志，表示该节点是否是某个单词的末尾。
2.  **`Trie` 类:**
* `__init__`: 创建 Trie 的根节点，它是一个 `TrieNode` 实例。
* `_char_to_index`: 一个辅助方法，将字符 'a' 到 'z' 转换为列表索引 0 到 25。
* `insert(word)`: 遍历单词的每个字符，通过 `_char_to_index` 找到对应的索引。如果当前节点的 `children` 列表在该索引处没有子节点，就创建一个新的 `TrieNode`。然后将当前节点移动到对应的子节点。单词遍历结束后，设置当前节点的 `is_end_of_word` 为 `True`。
* `search(word)`: 遍历单词的每个字符，通过索引在 `children` 列表中查找子节点。如果任一字符对应的子节点不存在（为 `None`），则单词不存在，返回 `False`。如果成功遍历完所有字符，最后检查当前节点的 `is_end_of_word` 标志。
* `startsWith(prefix)`: 遍历前缀的每个字符，通过索引在 `children` 列表中查找子节点。如果任一字符对应的子节点不存在，返回 `False`。如果能遍历完所有前缀字符，说明前缀路径存在，返回 `True`。

这种使用 `list` 的实现方式在处理固定且有限的字符集时比较高效，因为通过索引访问列表是 O(1) 操作。与使用字典相比，它的优点是查找更快，缺点是如果字符集很大或者稀疏，可能会浪费较多内存空间。对于小写英文字母，26 的长度是固定的，所以这是常见且有效的实现方式。
"""
