# ZigZag Conversion


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return(s)
        else:

            if len(s) % (numRows * 2 - 2) == 0:
                numColumns = (len(s) / (numRows * 2 - 2)) * 2
            elif len(s) % (numRows * 2 - 2) <= numRows:
                numColumns = (len(s) / (numRows * 2 - 2)) * 2 + 1
            else:
                numColumns = (len(s) / (numRows * 2 - 2)) * 2 + 2

            dic = {}
            k = 0
            for i in range(numColumns):
                for j in range(numRows):
                    if i % 2 == 0:
                        if k < len(s):
                            dic[(j, i)] = s[k]
                            k += 1
                        else:
                            dic[(j, i)] = ''

                    elif j != 0 and j != numRows - 1 and k < len(s):
                        dic[(numRows - j - 1, i)] = s[k]
                        k += 1
                    else:
                        dic[(numRows - j - 1, i)] = ''

            k, anslist = 0, []
            for i in range(numRows):
                for j in range(numColumns):
                    if dic[(i, j)] != '':
                        anslist.append(dic[(i, j)])

            ans = "".join(anslist)
            return(ans)


if __name__ == "__main__":
    print(Solution().convert("123456789", 2))
