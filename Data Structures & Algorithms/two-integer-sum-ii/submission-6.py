class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        input: target, array of integers, non-decreasing -> duplicates but also increases [1111] [11223]
        return: 2 indexes from input that add to target

        index1, index2 cannot equal

        input is sorted, binary search? 

        

        """
        
        l = 0
        r= len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
        return [l+1,r+1]
            