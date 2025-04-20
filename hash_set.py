from typing import List


def valid_anagram1(string1: str, string2: str) -> bool:
    """
    判断字符串是否是异位词使用排序 (leetcode.242)
    :param string1:
    :param string2:
    :return:
    """
    return sorted(string1) == sorted(string2)


def valid_anagram2(string1: str, string2: str) -> bool:
    """
    使用Counter类统计字符出现频率
    :param string1:
    :param string2:
    :return:
    """
    from collections import Counter
    return Counter(string1) == Counter(string2)


def valid_anagram3(string1: str, string2: str) -> bool:
    """
    hash表 统计字符出现次数
    :param string1:
    :param string2:
    :return:
    """
    from collections import defaultdict
    if len(string1) != len(string2):
        return False
    count = defaultdict(int)
    for char in string1:
        count[char] += 1
    for char in string2:
        count[char] -= 1
        if count[char] < 0:
            return False
    return True


def valid_anagram(string1: str, string2: str) -> bool:
    """
    使用数组简化版hash
    :param string1:
    :param string2:
    :return:
    """
    if len(string1) != len(string2):
        return False
    count = [0] * 26  # 固定空间 O(1)
    for char in string1:
        count[ord(char) - ord('a')] += 1
    for char in string2:
        count[ord(char) - ord('a')] -= 1
        if count[ord(char) - ord('a')] < 0:
            return False
    return True


def two_sum(nums: list[int], n: int) -> list:
    """
    leetcode.1 两数之和
    :param nums:
    :param n:
    :return:
    """
    if not nums:
        return []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums) - 1):
            if nums[i] + nums[j] == n:
                return [i, j]
    return []


def two_sum1(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        if (complement := target - num) in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i  # 字典里存储key是元素,value是索引
    return []


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    三数之和(leetcode.15) 使用hashSet
    问题描述：
    给定一个整数数组 nums，找出所有 不重复的三元组 [nums[i], nums[j], nums[k]]，
    使得 i != j != k 且 nums[i] + nums[j] + nums[k] = 0。
    :param nums:
    :return:
    """
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        # 跳过重复的元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        seen = set()
        for j in range(i + 1, n):
            complement = target - nums[j]
            if complement in seen:
                res.append([nums[i], complement, nums[j]])
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
    return res


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    三数之和(leetcode.15) 使用双指针
    问题描述：
    给定一个整数数组 nums，找出所有 不重复的三元组 [nums[i], nums[j], nums[k]]，
    使得 i != j != k 且 nums[i] + nums[j] + nums[k] = 0。
    :param nums:
    :return:
    """
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        left, right = i + 1, n - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[i], nums[left], nums[right]])
                # 左右指针多判断一位,看是否有重复元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 收集完结果后也要移动左右指针
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    return res

