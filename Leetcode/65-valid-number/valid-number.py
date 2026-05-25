class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()

        num = False
        exp = False
        sign = False
        dec = False

        for i in range(len(s)):

            # digit
            if s[i].isdigit():
                num = True

            # exponent
            elif s[i] in ['e', 'E']:

                # exponent already exists or no number before e
                if exp or not num:
                    return False

                exp = True
                num = False   # need number after e

            # sign
            elif s[i] in ['+', '-']:

                # sign allowed only at start or after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            # decimal point
            elif s[i] == '.':

                # decimal not allowed after exponent
                # or multiple decimals
                if dec or exp:
                    return False

                dec = True

            else:
                return False

        return num