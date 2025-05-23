"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

示例 1：

输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
示例 2：

输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
示例 3：

输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。
"""

def backspaceCompare(self, s: str, t: str) -> bool:
    s_stack = []
    t_stack = []

    for i in range(len(s)):
        if s[i] != '#':
            s_stack.append(s[i])
        else:
            if s_stack:
                s_stack.pop()
    
    for j in range(len(t)):
        if t[j] != '#':
            t_stack.append(t[j])
        else:
            if t_stack:
                t_stack.pop()
    
    if s_stack == t_stack:
        return True
    else:
        return False
