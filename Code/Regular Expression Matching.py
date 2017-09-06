# -*- coding: utf-8 -*-
class Solution(object):
    def isMatch1(self, ss, pp):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 预处理
        global s, p
        s = ss + '\n'
        p = pp + '\n'

        def match(sn, pn):
            if p[pn] == '\n':
                return s[sn] == '\n'

            else:
                if len(p) - pn == 1 or p[pn + 1] != "*":
                    if len(s) - 1 > sn and (s[sn] == p[pn] or p[pn] == '.'):
                        return match(sn + 1, pn + 1)
                    else:
                        return False
                else:
                    while sn < len(s) - 1 and (s[sn] == p[pn] or p[pn] == '.'):
                        if match(sn, pn + 2):
                            return True
                        else:
                            sn += 1
                    else:
                        return match(sn, pn + 2)

        return match(0, 0)

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False

        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

    def isMatch3(self, s, p):
        lenght = len(s)

        if lenght < len(p) - p.count('*') * 2:
            return False

        p += 'w'

        dp = [True] + [False] * lenght
        print dp
        for i in xrange(len(p) - 1):
            if p[i + 1] == '*':
                for j in range(lenght):
                    if not dp[j + 1]:
                        dp[j + 1] = dp[j] and (p[i] == s[j] or p[i] == '.')

            elif p[i] != '*':
                for j in reversed(range(1, lenght + 1)):
                    dp[j] = dp[j - 1] and (p[i] == s[j - 1] or p[i] == '.')
                dp[0] = False
            print p[i], dp

        return dp[-1]


if __name__ == '__main__':
    print(Solution().isMatch3("dddd", "d*"))
