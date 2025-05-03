"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

提示:
1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
"""
import unittest


# Definition for singly-linked list.
def is_anagram(s: str, t: str) -> bool:
    from collections import Counter
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


class TestIsAnagram(unittest.TestCase):

    def test_has_cycle(self):
        self.assertTrue(is_anagram(s="anagram", t="nagaram"))
        self.assertFalse(is_anagram(s="rat", t="car"))
        self.assertFalse(is_anagram(s="ra", t="car"))
