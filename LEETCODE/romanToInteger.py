class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_to_i = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        nums = [r_to_i[i] for i in s[::-1]]
        pre_val = None
        roman = 0
        for i in nums:
            if pre_val and pre_val > i:
                roman -= i
            else:
                roman += i
            pre_val = i
        
        return roman