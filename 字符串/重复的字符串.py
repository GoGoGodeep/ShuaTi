class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        index = (s + s).find(s, 1)  # 跳过第一个字符

        return index != len(s)
