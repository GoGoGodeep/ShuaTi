class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def is_true(start, end):
            if s[start] == '0' and start != end:
                return False
            
            num = int(s[start:end+1])
            return 0 <= num <= 255
        
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                result.append('.'.join(path))
                return

            if len(path) > 4:
                return
            
            for end in range(start, min(start + 3, len(s))):
                if is_true(start, end):
                    sub = s[start:end+1]
                    path.append(sub)
                    backtrack(end+1, path)
                    path.pop()
        
        backtrack(0, [])
        return result
