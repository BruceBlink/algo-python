"""
有效的括号（LeetCode.20）
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([])"
输出：true

:return:
"""
import unittest


def is_valid(string: str) -> bool:
    # 奇数长度肯定不匹配
    if len(string) % 2 != 0:
        return False
    m = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in string:
        if ch not in m:  # 不是右括号(是左括号)则进栈
            stack.append(ch)
        elif not stack or m[ch] != stack.pop():  # 栈不为空说明匹配不完,栈顶[全都是左括号]对应的右括号不能匹配
            return False
    return not stack


class TestMatchParenthesis(unittest.TestCase):

    def test_is_valid1(self):
        self.assertTrue(is_valid('()[]{}'))

    def test_is_valid2(self):
        self.assertFalse(is_valid('(]{}'))

    def test_is_valid3(self):
        self.assertTrue(is_valid('()'))

    def test_is_valid4(self):
        self.assertTrue(is_valid('([]{})'))

    def test_is_valid5(self):
        self.assertFalse(is_valid('())'))

    def test_is_valid6(self):
        self.assertTrue(is_valid('({[]})'))

    def test_is_valid7(self):
        self.assertFalse(is_valid(')('))

    def test_is_valid8(self):
        self.assertFalse(is_valid('[}'))

    def test_is_valid9(self):
        self.assertFalse(is_valid('}{'))
