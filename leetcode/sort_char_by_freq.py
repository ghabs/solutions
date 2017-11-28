from collections import Counter

class Solution(object):
    def frequencySort(self, arg):
        c = Counter(arg)
        return "".join(sorted(sorted(arg), key=lambda char: c[char], reverse=True))

if __name__ == "__main__":
    s = Solution()
    assert s.frequencySort("abb") == "bba"
    assert s.frequencySort("aBb") == "Bab"
    assert s.frequencySort("aAbb") == "bbAa"