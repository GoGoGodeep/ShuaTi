class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))

        for i in range(len(n) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if n[i] < n[i-1]:
                n[i - 1] = str(int(n[i - 1]) - 1)    # 将前一个字符减1

                # 将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质
                n[i:] = '9' * (len(n) - i)
        
        return int(''.join(n))
