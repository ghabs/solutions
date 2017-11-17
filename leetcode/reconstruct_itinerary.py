import collections
import copy

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.answers = []
        self.dep = {}
        def build_dep_graph(tickets):
          ticketdic = collections.defaultdict(list)
          for k, v in sorted(tickets)[::-1]:
              ticketdic[k].append(v)
          return ticketdic

        def dfs(dest):
            while self.dep[dest]:
                dfs(self.dep[dest].pop())
            self.answers.append(dest)
        self.dep = build_dep_graph(tickets)
        dfs("JFK")
        return self.answers[::-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
