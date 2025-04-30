class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0 
        # twenty = 0    # 可写可不写

        for i in bills:
            # 情况一：收到5美元
            if i == 5:
                five += 1

            # 情况二：收到10美元
            if i == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1
            
            # 情况三：收到20美元
            if i == 20:
                # 先尝试用10美元和5美元找零
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # twenty += 1
                    
                # 如果无法使用10美元找零，尝试用三张5美元找零
                elif five >= 3:
                    five -= 3
                    # twenty += 1
                else:
                    return False
            
        return True
