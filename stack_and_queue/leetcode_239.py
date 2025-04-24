"""
    滑动窗口最大值 (LeetCode 239)
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回 滑动窗口中的最大值 。

    示例 1：
    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]
    解释：
    滑动窗口的位置                   最大值
    -------------------------      -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    示例 2：
    输入：nums = [1], k = 1
    输出：[1]

    提示：
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
"""
import unittest


def max_sliding_window(nums: list[int], k) -> list[int]:
    """
    暴力解法
    """
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        current_max = -float('inf')
        for j in range(i, i + k):
            current_max = max(current_max, nums[j])
        res.append(current_max)
    return res


def max_sliding_window1(nums: list[int], k: int) -> list[int]:
    """
    单调队列解法 (虽然注释写了单调栈，但实际是用 deque 实现的单调队列)
    """
    # 处理输入数组为空的边缘情况
    if not nums:
        return []
    from collections import deque  # 通常使用 deque 来实现高效的双端队列操作
    res = []  # 存储每个窗口的最大值结果
    # 使用一个 deque 作为我们的单调队列，存储的是元素的索引
    # 队列中的索引 i 对应的 nums[i] 是单调递减的
    window = deque()

    # 遍历输入数组中的每一个元素及其索引 i
    for i, num in enumerate(nums):
        # ===== 处理窗口左边界 =====
        # 如果队列不为空，并且队列头部的索引 window[0] 已经超出了当前窗口的左边界 (i - k)
        # 例如，当前窗口是 [i-k+1, i]，那么 i-k 是窗口左边的前一个位置
        # 如果 window[0] <= i - k，说明它在当前窗口外面了
        if window and window[0] <= i - k:
            # 将队列头部的索引移除，因为它不再属于当前窗口
            window.popleft()  # deque 的高效移除头部操作 O(1)

        # ===== 维护队列的单调性 =====
        # 当队列不为空，并且当前遍历到的元素 num 大于或等于 队列尾部索引对应的元素 nums[window[-1]] 时：
        # 说明 nums[window[-1]] 这个元素不可能再成为它右边任何包含 num 的窗口的最大值了
        # 因为 num 更大（或相等且更靠右）
        while window and nums[window[-1]] <= num:
            # 将队列尾部的索引移除
            window.pop()  # deque 的高效移除尾部操作 O(1)

        # ===== 添加当前元素的索引 =====
        # 将当前元素的索引 i 加入队列尾部
        # 现在队列中存储的索引对应的元素是单调递减的
        window.append(i)

        # ===== 记录当前窗口的最大值 =====
        # 当窗口形成（即当前索引 i 达到了 k-1 或之后）时，我们开始记录最大值
        # i - k + 1 >= 0 判断当前窗口 [i-k+1, i] 是否是一个合法的窗口范围
        if i >= k - 1:  # 等价于 i - k + 1 >= 0
            # 队列头部的索引 window[0] 始终是当前窗口内的最大值的索引
            # 将该最大值 (nums[window[0]]) 添加到结果列表 res 中
            res.append(nums[window[0]])

    # 遍历完成后，res 列表中存储的就是每个滑动窗口的最大值
    return res


class TestMaxSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.nums = [1, 3, -1, -3, 5, 3, 6, 7]
        self.k = 3

    def test_max_sliding_window1(self):
        self.assertEqual(max_sliding_window1(self.nums, 3), [3, 3, 5, 5, 6, 7])

    def test_max_sliding_window(self):
        self.assertEqual(max_sliding_window(self.nums, 3), [3, 3, 5, 5, 6, 7])
