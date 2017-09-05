class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        numdic = {'1': 1, '2': 2,
                  '3': 3, '4': 4,
                  '5': 5, '6': 6,
                  '7': 7, '8': 8,
                  '9': 9, '0': 0,
                  }

        str += '*'
        ans, mark, k = 0, 1, True

        for i in str:
            if k and (i == ' ' or i == '+' or i == '-'):
                if i == '+':
                    k = False
                elif i == '-':
                    k = False
                    mark = -1

            else:
                if i in numdic:
                    k = False
                    ans = ans * 10 + numdic[i]

                else:
                    ans *= mark
                    if ans < -2147483648:
                        return(-2147483648)
                    elif ans > 2147483647:
                        return(2147483647)
                    else:
                        return(ans)


if __name__ == '__main__':
    print(Solution().myAtoi('-111a11111111111111111111111111111111'))
