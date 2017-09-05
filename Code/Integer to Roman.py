# Integer to Roman


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic_type = {
            3: ('I', 'V', 'X'),
            2: ('X', 'L', 'C'),
            1: ('C', 'D', 'M'),
            0: ('M', '*', '#'),
        }

        dic_num = {
            0: '',
            1: '{i}',
            2: '{i}{i}',
            3: '{i}{i}{i}',
            4: '{i}{v}',
            5: '{v}',
            6: '{v}{i}',
            7: '{v}{i}{i}',
            8: '{v}{i}{i}{i}',
            9: '{i}{x}',
        }
        list = []
        n, x = 0, 3
        while x > -1:
            num -= 10 ** x
            if num >= 0:
                n += 1
            else:
                num += 10 ** x
                list.append(n)
                n = 0
                x -= 1

        print list

        s = ''
        for num, i in enumerate(list):

            s += dic_num[i].format(
                i=dic_type[num][0],
                v=dic_type[num][1],
                x=dic_type[num][2],
            )

        return(s)


if __name__ == '__main__':
    print(Solution().intToRoman(3999))
