class Solution:
    def captcha_one(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        summed, end = 0, len(nums) - 1
        for index, value in enumerate(nums):
            if index == end:
                if value == nums[0]:
                    summed += int(value)
                return summed
            if value == nums[index+1]:
                summed += int(value)

    def captcha_two(self, nums):
        summed, end = 0, len(nums)
        step = end // 2
        for index, value in enumerate(nums):
            if value == nums[(index + step) % end]:
                summed += int(value)
        return summed

if __name__ == "__main__":
    s = Solution()
    assert 3 == s.captcha_one("1122")
    assert 4 == s.captcha_one("1111")
    assert 9 == s.captcha_one("91212129")
    assert 0 == s.captcha_one("1234")
    assert 6 == s.captcha_two("1212")
    assert 0 == s.captcha_two("1221")
    assert 4 == s.captcha_two("12131415")