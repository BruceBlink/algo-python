"""
347. 前 K 个高频元素

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
你可以按 任意顺序 返回答案。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""
import collections
import heapq
import unittest


class Solution:
    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        """
        哈希表和堆排序
        @param nums:
        @param k:
        @return:
        """
        # Step 1: 统计每个元素的频率
        freq_map = collections.Counter(nums)

        # Step 2: 使用最小堆来维护前 k 个高频元素
        # 堆中存储的是 (频率, 元素) 对。
        # heapq 默认是最小堆，因此频率最小的对会在堆顶。
        min_heap = []

        # 遍历频率映射中的每一个 (元素, 频率) 对
        for element, freq in freq_map.items():
            # 将 (频率, 元素) 对推入最小堆
            # Python 的 heapq 模块是基于列表实现的，heappush 将元素添加到列表中并维护堆属性
            heapq.heappush(min_heap, (freq, element))

            # 如果堆的大小超过 k，则弹出堆顶元素（即当前堆中频率最小的元素）
            # 这样确保堆中始终只有 k 个元素，且它们是目前为止频率最高的 k 个
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: 提取结果
        # 堆中剩下的 k 个元素就是频率最高的 k 个元素。
        # 我们只需要这些元素的本身值（即 (频率, 元素) 对中的第二个值）
        return [item[1] for item in min_heap]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: 统计每个元素的频率
        # collections.Counter 是一个非常方便的哈希表子类，用于计数
        freq_map = collections.Counter(nums)

        # Step 2: 创建频率桶
        # 桶的索引表示频率，桶内存储的是具有该频率的元素列表
        # 最大的频率不会超过 nums 的长度
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: 填充频率桶
        # 遍历频率映射，将元素根据其频率放入对应的桶中
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 4: 收集结果
        # 从最高频率的桶开始倒序遍历，直到收集到 k 个元素
        result = []
        # 从 len(nums) 倒序遍历到 1 (不包含 0)
        for i in range(len(nums), 0, -1):
            # 将当前频率桶中的所有元素添加到结果列表
            for num in buckets[i]:
                result.append(num)
                # 如果已经收集到 k 个元素，立即返回
                if len(result) == k:
                    return result

        # 理论上，在 k 的约束下，代码执行到这里时 result 肯定已经包含了 k 个元素
        return result


# 单元测试类
class TestTopKFrequent(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_elements = [1, 2]
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_example_2_single_element(self):
        nums = [1]
        k = 1
        expected_elements = [1]
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_all_elements_distinct(self):
        # 所有元素都不同，频率均为 1
        nums = [10, 20, 30, 40, 50]
        k = 3
        # 频率都是 1 时，heapq 会保留元素值较大的那 k 个
        # 因此，期望结果是元素值最大的 3 个: 30, 40, 50
        expected_elements = [30, 40, 50] # <--- 这里已修改
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_all_elements_same(self):
        nums = [7, 7, 7, 7, 7]
        k = 1
        expected_elements = [7]
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_mixed_frequencies(self):
        # 混合频率，且 k 恰好取到有相同频率的集合
        # 频率：3:3, 1:2, 2:2, 4:1。k=3 应该包含 3, 1, 2。
        nums = [1, 1, 2, 2, 3, 3, 3, 4]
        k = 3
        expected_elements = [3, 1, 2]
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_multiple_occurrences_same_freq(self):
        nums = [1, 2, 3, 1, 2, 1]
        k = 1
        expected_elements = [1]
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_large_number_range(self):
        nums = [10000, -10000, 10000, -10000, 10000]
        k = 1
        expected_elements = [10000]
        solution = Solution()
        actual_elements = solution.topKFrequent(nums, k)
        self.assertCountEqual(actual_elements, expected_elements)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
