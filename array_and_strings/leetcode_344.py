"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。


示例 1：

输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]


提示：

1 <= s.length <= 10^5
s[i] 都是 ASCII 码表中的可打印字符
"""
import unittest


def reverse_string(s: list[str]) -> list[str]:
    if not s:
        return s
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string(["h", "e", "l", "l", "o"]), ["o", "l", "l", "e", "h"])
        self.assertTrue(reverse_string(["H", "a", "n", "n", "a", "h"]), ["h", "a", "n", "n", "a", "H"])
