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
        return -1, -1 # 没有空的单元格

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
                    return True # 如果递归调用返回True，表示找到一个完整的解
                # 如果递归调用返回False 说明数字不满足条件，要回溯,删除已经填入的数字
                remove_number(_r, _c, _num)
        # 如果所有的数字都没有扎到解，返回False
        return False

    # 从第一个空单元格开始
    backtrack()
