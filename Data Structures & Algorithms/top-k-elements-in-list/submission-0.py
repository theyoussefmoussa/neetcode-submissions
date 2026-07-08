class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = {}

        for num in nums:
            if num in counts_dict:
                counts_dict[num] += 1
            else:
                counts_dict[num] = 1

        sorted_items = sorted(
            counts_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result