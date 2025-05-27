"""
55. 跳跃游戏

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


提示：

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        # 初始的目标位置就是数组的最后一个下标
        last_good_index_pos = n - 1

        # 从倒数第二个位置开始，向前遍历到第一个位置 (下标 0)
        # range(start, stop, step)
        # start = n - 2 (倒数第二个位置)
        # stop = -1 (到 0 停止，不包含 -1)
        # step = -1 (每次向前移动一步)
        for i in range(n - 2, -1, -1):
            # 如果从当前位置 i 加上它的跳跃长度 nums[i]
            # 能够到达或越过当前的 last_good_index_pos
            if i + nums[i] >= last_good_index_pos:
                # 那么当前位置 i 就成为了一个新的“好位置”（即新的目标位置）
                last_good_index_pos = i

        # 循环结束后，如果 last_good_index_pos 变成了 0，
        # 说明从起始位置 (下标 0) 可以到达最终目标位置
        return last_good_index_pos == 0
