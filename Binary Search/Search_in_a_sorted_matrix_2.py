class Solution:
    def searchMatrix(self, matrix ,target):
        row , col = len(matrix) , len(matrix[0])

        x, y = row-1 , 0

        while(True):
            if x < 0 or y >= col:
                break

            curr_element = matrix[x][y]

            if target > curr_element:
                y += 1

            elif target < curr_element:
                x -= 1

            else:
                return True

        return False


obj = Solution()

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

ans = obj.searchMatrix(matrix , target)
print(ans)
