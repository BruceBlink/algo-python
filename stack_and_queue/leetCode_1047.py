"""
删除字符串中的所有相邻重复项（LeetCode 1047）
给出由小写字母组成的字符串 s，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 s 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

提示：
1 <= s.length <= 105
s 仅由小写英文字母组成。

:param string:
:return:
"""
import unittest


def remove_duplicates(string: str) -> str:
    stack = []
    for c in string:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


def remove_duplicates1(self, s: str) -> str:
    """
    删除字符串中的所有相邻重复项 (双指针/原地构建思路)
    使用列表作为缓冲区，i 指向下一个写入位置
    """
    res = []  # 使用列表作为结果缓冲区
    i = 0  # i 指向 res 中下一个可以写入字符的位置

    for char in s:
        # 如果 res 不为空 (i > 0) 并且 res 的最后一个字符 (res[i-1]) 和当前字符相同
        if i > 0 and res[i - 1] == char:
            i -= 1  # 模拟删除 res 的最后一个字符，将写指针前移
        else:
            # 否则，将当前字符写入 res 的当前位置
            # 如果 i 等于 res 的长度，说明需要在末尾添加
            if i == len(res):
                res.append(char)
            else:
                res[i] = char
            i += 1  # 写指针后移

    # 最终结果是 res 从开始到 i 位置的部分
    return "".join(res[:i])


# 递归方法 (效率低，可能栈溢出，不适合 LeetCode)
def remove_duplicates_recursive(s: str) -> str:
    # 扫描字符串查找相邻重复项
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            # 找到一对，删除它们，然后对新字符串递归
            new_s = s[:i] + s[i + 2:]
            return remove_duplicates_recursive(new_s)
    # 如果没有找到相邻重复项，返回当前字符串
    return s


# 字符串替换循环方法 (效率低)
def remove_duplicates_replace(s: str) -> str:
    while True:
        found = False
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            duplicate_pair = char * 2  # 例如 "aa", "bb" 等
            if duplicate_pair in s:
                s = s.replace(duplicate_pair, "")
                found = True
                break  # 从头开始再次检查，因为可能有新的相邻重复项出现

        if not found:  # 如果一轮扫描下来没有发现任何重复项
            break
    return s
# 注意：这种方法每次 replace 都可能生成新字符串并重新扫描，效率也较低。


class TestDailyTemperature(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates('122433'), '14')
