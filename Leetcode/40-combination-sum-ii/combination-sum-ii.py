class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        # Sorting helps skip duplicates
        candidates.sort()

        def backtrack(start, path, target):

            # Found valid combination
            if target == 0:
                result.append(path[:])
                return

            # Invalid path
            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose current number
                path.append(candidates[i])

                # Move to next index
                backtrack(
                    i + 1,
                    path,
                    target - candidates[i]
                )

                # Backtrack
                path.pop()

        backtrack(0, [], target)

        return result