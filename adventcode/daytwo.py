from adventimport import ImportData

class Solution:
    def checksum(self, data):
        summed = 0
        for r in data:
            maxn, minn = 0, 99999999999
            for i in r:
                maxn = max(int(i), maxn)
                minn = min(int(i), minn)
            summed += (maxn - minn)
        return summed
    
    def checksum_two(self, data):
        summed = 0
        for r in data:
            for i in r:
                for j in r:
                    if (int(j)%int(i) == 0) and i != j:
                        summed += (int(j)/int(i)) 
        return summed      

if __name__ == "__main__":
    data = ImportData().text_import("data/two.txt")
    s = Solution()
    print(s.checksum([[1,2,3],[2,6]]))
    print(s.checksum_two(data))
    print(s.checksum_two([[2,4],[2,6]]))
