"""
402. 移掉 K 位数字
给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，
使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
示例 1 ：

输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
示例 2 ：

输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 ：

输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。


提示：

1 <= k <= num.length <= 105
num 仅由若干位数字（0 - 9）组成
除了 0 本身之外，num 不含任何前导零
"""
import unittest


def remove_k_digits(num: str, k: int) -> str:
    stack = [] # 使用列表作为栈

    # 遍历数字字符串中的每一个位
    for digit in num:
        # 当栈不为空、还有移除次数 (k > 0)、且当前位小于栈顶部时
        # 弹出栈顶部元素 (贪婪地移除较大的位)
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        # 将当前位推入栈
        stack.append(digit)

    # 如果还有剩余的移除次数，移除栈末尾的 k 个位
    # 这发生在栈中剩余的位是单调不减的情况下
    while k > 0:
        stack.pop()
        k -= 1

    # 将栈中的位连接成结果字符串
    result = "".join(stack)

    # 移除前导零。如果移除前导零后结果为空，则返回 "0"。
    # [i:] 切片从第一个非零位开始。
    i = 0
    while i < len(result) and result[i] == '0':
        i += 1

    # 返回结果，同时处理移除后字符串为空的情况
    return result[i:] if i < len(result) else "0"


class TestRemoveKDigits(unittest.TestCase):

    def test_sum_sub_array_mins_brute_force(self):
        self.assertEqual(remove_k_digits(num="1432219", k=3), "1219")
        self.assertEqual(remove_k_digits(num="10", k=2), "0")
        self.assertEqual(remove_k_digits(num="10200", k=1), "200")
        self.assertEqual(remove_k_digits(num="12345", k=2), "123")
        self.assertEqual(remove_k_digits(num="98765", k=3), "65")
        self.assertEqual(remove_k_digits(num="10", k=1), "0")
        self.assertEqual(remove_k_digits(num="112", k=1), "11")
