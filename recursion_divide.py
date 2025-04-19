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


