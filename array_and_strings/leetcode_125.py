"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。



示例 1：

输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
示例 2：

输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
示例 3：

输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。


提示：

1 <= s.length <= 2 * 10^5
s 仅由可打印的 ASCII 字符组成
"""
import unittest


def is_palindrome(s: str) -> bool:
    """
    验证回文串（双指针）
    """
    # 如果字符串为空，根据题目定义是回文串
    if not s:
        return True

    left, right = 0, len(s) - 1

    # 当左指针在右指针左边时循环
    while left < right:
        # 从左边找到第一个字母数字字符
        while left < right and not s[left].isalnum():
            left += 1

        # 从右边找到第一个字母数字字符
        while left < right and not s[right].isalnum():
            right -= 1

        # 如果移动指针后 left 已经 >= right，说明剩余部分是空或单个字符，是回文
        # 这个检查也可以放在 while 循环外部或只在内部判断后 break
        # 这里的判断可以避免后续在 left >= right 时进行不必要的比较
        if left >= right:
            break # 或者 return True (如果逻辑需要在这里结束)

        # 比较左右两个字母数字字符，忽略大小写
        if s[left].lower() != s[right].lower():
            # 如果不相等，则不是回文串，返回 False
            return False

        # 如果相等，则继续向内移动指针
        left += 1
        right -= 1

    # 如果循环正常结束，没有发现不匹配的情况，说明是回文串
    return True


class TestTwoSums(unittest.TestCase):

    def test_two_sum(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome(".,"))
