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
