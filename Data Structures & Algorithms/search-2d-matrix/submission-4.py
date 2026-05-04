class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break   
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        left,right = 0, len(matrix[0]) - 1

        while left <= right:
            colmid = (left + right) // 2
            if matrix[mid][colmid] == target:
                return True
            elif matrix[mid][colmid] < target:
                left = colmid + 1
            else:
                right = colmid - 1    

        return False    
        