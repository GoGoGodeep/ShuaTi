def totalFruit(self, fruits: List[int]) -> int:
    from collections import Counter

    counter = Counter()

    left = 0
    max_len = 0

    for right in range(len(fruits)):
        counter[fruits[right]] += 1

        while len(counter) > 2:
            counter[fruits[left]] -= 1

            if counter[fruits[left]] == 0:
                counter.pop(fruits[left])
            
            left += 1
        
        max_len = max(max_len, right - left + 1)

    return max_len
