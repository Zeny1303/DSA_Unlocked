class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        result = []
        i = 0

        while i < len(words):

            line = []
            line_length = 0

            # collect words for current line
            while (i < len(words) and
                   line_length + len(words[i]) + len(line) <= maxWidth):

                line.append(words[i])
                line_length += len(words[i])
                i += 1

            spaces = maxWidth - line_length
            gaps = len(line) - 1

            # last line OR single word line
            if i == len(words) or gaps == 0:

                justified = " ".join(line)
                justified += " " * (maxWidth - len(justified))

            else:

                even_spaces = spaces // gaps
                extra_spaces = spaces % gaps

                justified = ""

                for j in range(gaps):

                    justified += line[j]

                    # extra spaces go to left gaps first
                    justified += " " * (
                        even_spaces + (1 if j < extra_spaces else 0)
                    )

                justified += line[-1]

            result.append(justified)

        return result