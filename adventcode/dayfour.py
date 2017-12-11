from collections import Counter
cat = ''.join

"note: this is from Norvig's solution"
def canon(items, typ=None):
    "Canonicalize these order-independent items into a hashable canonical form."
    typ = typ or (cat if isinstance(items, str) else tuple)
    return typ(sorted(items))

class Solution:
    def import_passphrases(self):
        counter = 0
        with open("input.txt", 'r') as f:
            for line in f:
                l = line.split()
                if len(l) == len(set(l)):
                    print(l)
                    counter += 1
        print(counter)

    def import_passphrases_2(self):
        counter = 0
        with open("input.txt", 'r') as f:
            for line in f:
                l = line.split()
                if len (l) == len(set(tuple(map(canon, l)))):
                    counter+= 1
                #print(c)

        print(counter)

if __name__ == "__main__":
    Solution().import_passphrases_2()