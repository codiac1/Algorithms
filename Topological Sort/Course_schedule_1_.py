from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_order = []
        indegree = {}
        graph = {}
        
        for i in range(numCourses):
            indegree[i] = 0
            graph[i] = []
            
        q = deque()
        for courses in prerequisites:
            parent = courses[1]
            child = courses[0]
            indegree[child] += 1
            graph[parent].append(child)
            
        for vertex in indegree:
            if indegree[vertex] == 0:
                q.append(vertex)
                
        while(q):
            vertex = q.popleft()
            sorted_order.append(vertex)
            children = graph[vertex]
            for child in children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        if len(sorted_order) == numCourses:
            return True
        return False
            

        
