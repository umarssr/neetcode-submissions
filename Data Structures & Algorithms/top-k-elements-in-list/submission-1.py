class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        print(count)
        for number, count in count.items():
            freq[count].append(number)
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

