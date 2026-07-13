from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ordered = sorted(count.keys(), key=lambda n: count[n], reverse = True)
        return ordered[:k]