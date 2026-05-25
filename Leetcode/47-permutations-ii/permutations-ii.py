class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        # Sorting helps detect duplicates
        nums.sort()

        used = [False] * len(nums)

        def backtrack(path):

            # Complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                # Skip already used elements
                if used[i]:
                    continue

                # Skip duplicates
                if (
                    i > 0 and
                    nums[i] == nums[i - 1] and
                    not used[i - 1]
                ):
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                # Backtrack
                path.pop()
                used[i] = False

        backtrack([])

        return result