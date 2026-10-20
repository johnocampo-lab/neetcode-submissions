class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force solution - O(n^2) time
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Sorting approach - O(n log n) time
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

        # Optimal approach using a Hash Set - O(n) time, O(n) space
        mySet = set()

        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)

        return False