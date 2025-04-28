"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。


提示：

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
import unittest


def three_sum(nums: list[int]) -> list[list[int]]:
    # 结果列表
    result = []
    # 获取数组长度
    n = len(nums)

    # 0. 排序数组
    nums.sort()

    # 1. 遍历数组，固定第一个数 (用 i 指针)
    # 遍历到倒数第三个元素即可，因为后面至少需要两个元素组成三元组
    for i in range(n - 2):
        # 如果当前元素 nums[i] > 0，则后面的元素都 >= nums[i]，和不可能为 0，直接提前结束
        if nums[i] > 0:
            break

        # 跳过重复的第一个元素，避免生成重复的三元组
        # i > 0 是为了防止索引越界
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 2. 使用双指针在 i 后面的子数组中查找另外两个数
        left = i + 1  # 左指针，从 i 的下一个位置开始
        right = n - 1  # 右指针，从数组末尾开始

        # 当左指针在右指针左边时循环
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # 找到了和为 0 的三元组
            if current_sum == 0:
                # 将找到的三元组加入结果列表
                result.append([nums[i], nums[left], nums[right]])

                # 3. 跳过重复的第二个和第三个数
                # 移动左指针，跳过所有与当前 nums[left] 相同的元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # 移动右指针，跳过所有与当前 nums[right] 相同的元素
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 继续查找，移动 left 和 right 指针
                left += 1
                right -= 1

            # 当前和小于 0，需要增大和，移动左指针
            elif current_sum < 0:
                left += 1
            # 当前和大于 0，需要减小和，移动右指针
            else:  # current_sum > 0
                right -= 1

    # 返回所有找到的不重复三元组
    return result


class TestThreeSum(unittest.TestCase):

    def test_move_zeroes(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], three_sum(nums=[-1, 0, 1, 2, -1, -4]))
        self.assertEqual([], three_sum([0, 1, 1]))
        self.assertEqual([[0, 0, 0]], three_sum(nums=[0, 0, 0]))
        self.assertEqual([[-2, 0, 2], [-2, 1, 1]], three_sum(nums=[-2, 0, 1, 1, 2]))
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], three_sum(nums=[-4, -1, -1, 0, 1, 2]))
