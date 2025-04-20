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
