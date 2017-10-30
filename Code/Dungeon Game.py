# Dungeon Game


class Solution(object):
    def calculateMinimumHP1(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        def go(hp, i, j):
            # check end
            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                return True

            left, below = False, False

            # go to the left room
            if j != len(dungeon[0]) - 1:
                if dungeon[i][j + 1] + hp > 0:
                    left = go(hp + dungeon[i][j + 1], i, j + 1)

            # go to the below room
            if i != len(dungeon) - 1:
                if dungeon[i + 1][j] + hp > 0:
                    below = go(hp + dungeon[i + 1][j], i + 1, j)

            return (left or below)

        if dungeon[0][0] > 0:
            hp = 1
        else:
            hp = 1 - dungeon[0][0]

        while 1:
            if go(hp + dungeon[0][0], 0, 0):
                return hp
            else:
                hp += 1

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        ans = [[0 for j in xrange(len(dungeon[0]))]
               for i in xrange(len(dungeon))]

        for i in xrange(len(dungeon) - 1, -1, -1):
            for j in xrange(len(dungeon[0]) - 1, -1, -1):
                if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                    left = below = 1

                else:
                    left = 2 ** 32 if i == len(dungeon) - 1 else ans[i + 1][j]
                    below = 2 ** 32 if j == len(dungeon[0]) - \
                        1 else ans[i][j + 1]

                temp = min(left, below) - dungeon[i][j]
                ans[i][j] = 1 if temp < 1 else temp

        for i in ans:
            print i
        return ans[0][0]


if __name__ == '__main__':
    print Solution().calculateMinimumHP([[2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    # [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
