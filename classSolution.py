class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            list = nums
            list.append(target)
            list.sort() 
            return list.index(target)



sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))
print(sol.searchInsert([1, 3, 5, 6], 2)) 
print(sol.searchInsert([1, 3, 5, 6], 7))
