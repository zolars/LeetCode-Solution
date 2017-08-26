# Longest substring with at most k distinct characters


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lookup = {}
        maxlenght = 0
        left = 0

        for i, char in enumerate(s):
            if char in lookup:
                lookup[char] = i
            else:
                if len(lookup) == k:
                    sorten = sorted(lookup.iteritems(), key=lambda d: d[1])
                    del lookup[sorten[0][0]]
                    if len(sorten) > 1:
                        left = sorten[1][1]
                    else:
                        left = i
                    lookup[char] = i
                else:
                    lookup[char] = i
            maxlenght = max(maxlenght, i - left + 1)
        else:
            return(maxlenght)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct('asdfafsbfilbbsfn', 1))
