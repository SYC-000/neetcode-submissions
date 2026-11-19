from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        return list(reversed(list(dict(sorted(count.items(), key=lambda x: x[1])).keys())[-k:]))