class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) :
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2 , nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if not nums1:
            if n2%2 == 0:
                return (nums2[n2//2] + nums2[n2//2 -1])/2.0
            else:
                return nums2[n2//2]
        
        low = 0 
        high = n1

        while(low <= high):
            part1 = (low+high)//2
            part2 = (n1+n2+1)//2 - part1 
            
            if part1 == 0:
                l1 = -math.inf
            else:
                l1 = nums1[part1-1]
            
            if part2 == 0:
                l2 = -math.inf
            else:
                l2 = nums2[part2-1]
            
            if part1 == n1:
                r1 = math.inf
            else:
                r1 = nums1[part1]
            
            if part2 == n2:
                r2 = math.inf
            else:
                r2 = nums2[part2]
            
            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 != 0:
                    return max(l1 , l2)
                else:
                    return (max(l1 , l2) + min(r1 , r2))/2.0
            
            elif l1 > r2:
                high = part1 - 1
            
            else:
                low = part1 + 1
        
        return 0.0
        
        