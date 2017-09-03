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


if __name__ == '__main__':
    print(Solution().isMatch1("aab", "a*c*a*ab"))
