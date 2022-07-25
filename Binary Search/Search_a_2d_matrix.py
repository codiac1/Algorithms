class Solution:
    def bsearch_row(self , matrix ,target, low, high):
        while(low<=high):
            mid = (low+high)//2
            if matrix[mid][0] <= target:
                if matrix[mid][-1] >= target:
                    return mid
                else:
                    low = mid+1
            else:
                high = mid-1
        return 0

    def bsearch_target(self, arr,ele,  low, high):
        while(low<=high):
            mid = (low+high)//2
            if arr[mid] == ele:
                return True
            elif arr[mid] > ele:
                high = mid-1
            else:
                low = mid+1
        return False
                
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if cols == 1 and rows == 1:
            if matrix[rows-1][cols-1] == target:
                return True
            return False
        row_no = self.bsearch_row(matrix, target, 0 , rows-1)
        return self.bsearch_target(matrix[row_no] ,target,0,cols-1)
        