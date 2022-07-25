# This is not from Topological Sort but thought of adding all three problems here


from heapq import *
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x : x[1] )
        
        max_heap = []
        total_days = 0    
        
        for course in courses :
            heappush(max_heap , -(course[0]))
            total_days = total_days + course[0]
            if total_days > course[1]:
                duration = -1*heappop(max_heap)
                total_days -= duration
    
        return len(max_heap)
