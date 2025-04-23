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
    stack = []
    # 右括号映射到其对应的左括号
    mapping = {")": "(", "]": "[", "}": "{"}
    for ch in string:
        # 如果是左括号，压入栈
        if ch in mapping.values():  # 检查 ch 是否是某个右括号对应的“值”（即左括号）
            stack.append(ch)
        # 如果是右括号
        elif ch in mapping.keys():  # 检查 ch 是否是某个右括号的“键”（即右括号本身）
            # 检查栈是否为空 (没有左括号可匹配)
            # 或者栈顶元素不是当前右括号期望的左括号
            if not stack or mapping[ch] != stack.pop():  #
                return False
        # 处理既不是左括号也不是右括号的字符，如果题目保证只有括号，这段可以省略
        # else:
        #     pass # 或者 raise ValueError("Invalid character in string")

    # 遍历完成后，检查栈是否为空。如果栈为空，所有左括号都匹配了。
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
