class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses ==1 :
            return [0]
        
        sorted_order = []
        indegree = {}
        graph = {}
        
        for i in range(numCourses):
            indegree[i] = 0
            graph[i] = []
            
        for courses in prerequisites:
            parent = courses[1]
            child = courses[0]
            graph[parent].append(child)
            indegree[child] += 1
         
        q = deque()
        for course in indegree:
            if indegree[course] == 0:
                q.append(course)
        
        while(q):
            vertex = q.popleft()
            sorted_order.append(vertex)
            children = graph[vertex] 
            for child in children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        if len(sorted_order)==numCourses:
            return sorted_order
        return []
            
            
