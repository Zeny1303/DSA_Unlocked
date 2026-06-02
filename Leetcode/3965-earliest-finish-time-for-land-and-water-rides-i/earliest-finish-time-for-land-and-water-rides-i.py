class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        def calc(start1, dur1, start2, dur2):
            ans = float('inf')

            for i in range(len(start1)):
                first_finish = start1[i] + dur1[i]

                for j in range(len(start2)):
                    second_start = max(first_finish, start2[j])
                    second_finish = second_start + dur2[j]

                    ans = min(ans, second_finish)

            return ans

        # Land -> Water
        option1 = calc(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        # Water -> Land
        option2 = calc(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(option1, option2)