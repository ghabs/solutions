class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM", "MMMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

if __name__ == "__main__":
    sol = Solution()
    assert "IV" == sol.intToRoman(4)
    assert "IX" == sol.intToRoman(9)
    assert "III" == sol.intToRoman(3)
    assert "XLIX" == sol.intToRoman(49)
    assert "DXII" == sol.intToRoman(512)