#
# @lc app=leetcode.cn id=809 lang=python3
#
# [809] 情感丰富的文字
#

# @lc code=start
import re
from itertools import groupby


class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        pattern = (
            "^"
            + "".join(
                f"{re.escape(c)}{{1,{n}}}" if n > 2 else f"{re.escape(c)}{{{n}}}"
                for c, n in ((k, sum(1 for _ in g)) for k, g in groupby(s))
            )
            + "$"
        )
        reg = re.compile(pattern)
        return sum(bool(reg.fullmatch(w)) for w in words)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.expressiveWords(
        s="heeellooo",
        words=["hello", "hi", "helo"],
    )
    print(ans)
