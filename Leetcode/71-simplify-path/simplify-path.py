class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        parts = path.split('/')

        for part in parts:

            # ignore empty and current directory
            if part == '' or part == '.':
                continue

            # go back to parent directory
            elif part == '..':
                if stack:
                    stack.pop()

            # valid directory name
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
        