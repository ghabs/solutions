import re
import collections

class Solution:
    def parse_input(self):
        children = set()
        have_children = set()
        with open("data/seven.txt", 'r') as f:
            for line in f:
                check = re.search("->", line)
                if check:
                    l = re.split("->", line)
                    chi = l[1].split(",")
                    for c in chi:
                        children.add(c.strip())
                    hc = l[0].split(" ")[0]
                    have_children.add(hc)
        return children, have_children

    def parse_get_weight(self):
        children = dict()
        have_children = dict()
        weights = dict()
        with open("data/seven.txt", 'r') as f:
            for line in f:
                check = re.search("->", line)
                if check:
                    l = re.split("->", line)
                    chi = l[1].split(",")
                    hcl = l[0].split(" ")
                    children[hcl[0]] = list(map(str.strip, chi))
                    have_children[hcl[0]] = int(hcl[1][1:-1]) 
                t = re.split(" ", line)
                weights[t[0]] = int((t[1]).rstrip('\n')[1:-1])
        return children, have_children, weights

    def elimination(self, children, have_children):
        #if no children, remove
        #if in other nodes child array, remove
        for s in have_children:
            if s not in children:
                return s

    def calculate_weight_subtree(self, elem, children, have_children, weights):
        val = 0
        if elem not in have_children:
            return weights[elem]
        for e in children[elem]:
            val += self.calculate_weight_subtree(e, children, have_children, weights) 
        return weights[elem] + val

    def sum_weight(self, children, have_children, weights, root):
        count = collections.Counter()
        # memoize
        # cache = dict()
        for s,c in have_children.items():
             val = self.calculate_weight_subtree(s, children, have_children, weights)
             count[s] += val
        elem, off = self.traverse_for_incorrect(root, count, children)
        return elem

    def traverse_for_incorrect(self, root, weights, children):
        check = collections.defaultdict(list)
        for elem in children[root]:
            check[weights[elem]].append(elem)
        for k,v in check.items():
            if len(v) == 1:
              el, mc = self.traverse_for_incorrect(v[0], weights, children)
              return el, mc   
        return root, check

        
        # return least common
            


if __name__ == "__main__":
    s = Solution()
    c, hc = s.parse_input()
    root = (s.elimination(c, hc))
    h, hc, w = s.parse_get_weight()
    print(s.sum_weight(h, hc, w, root))
