class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        #print(d)
        count = 0
        
        for num in nums:
            if d[num] > 0:
                count += 1
                d[num] -= 1
            else:
                d[k-num] += 1            
        return count
        