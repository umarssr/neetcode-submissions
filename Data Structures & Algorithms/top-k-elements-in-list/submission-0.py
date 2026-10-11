class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myhash = {}
        for num in nums:
            if num in myhash:
                myhash[num] +=1
            else:
                myhash[num] = 1
        sorted_items = sorted(myhash.items(), key = lambda item: item[1], reverse = True)
        top_k =sorted_items[:k]
        res = []
        for num,value in top_k:
            res.append(num)
        return res
        