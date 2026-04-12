class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        c0 = s.count('0')
        c1 = s.count('1')

        # pos array (balance -> list of indices)
        pos = [[] for _ in range(2 * n + 5)]
        offset = n + 2

        # initial balance = 0 at index -1
        pos[offset].append(-1)

        cur = 0

        # build prefix balance positions
        for i in range(n):
            if s[i] == '1':
                cur += 1
            else:
                cur -= 1
            pos[cur + offset].append(i)

        ans = 0
        cur = 0

        for i in range(n):
            if s[i] == '1':
                cur += 1
            else:
                cur -= 1

            # Case 1: exact balance
            if pos[cur + offset]:
                j = pos[cur + offset][0]
                if j < i:
                    ans = max(ans, i - j)

            # Case 2: +2 imbalance (extra 1s)
            idx = cur - 2 + offset
            if 0 <= idx < len(pos):
                for j in pos[idx]:
                    if j >= i:
                        break
                    length = i - j
                    z = (length - 2) // 2
                    if c0 > z:
                        ans = max(ans, length)
                        break

            # Case 3: -2 imbalance (extra 0s)
            idx = cur + 2 + offset
            if 0 <= idx < len(pos):
                for j in pos[idx]:
                    if j >= i:
                        break
                    length = i - j
                    o = (length - 2) // 2
                    if c1 > o:
                        ans = max(ans, length)
                        break

        return ans