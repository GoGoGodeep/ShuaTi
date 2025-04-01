class Solution:
    def canConstruct(self, ransomNote, magazine):
        from collections import defaultdict

        has_set = defaultdict(int)
        for char in magazine:
            has_set[char] += 1

        for char in ransomNote:
            val = has_set.get(char)
            if not val:
                return False
            else:
                has_set[char] -= 1

        return True
