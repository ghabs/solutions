from collections import defaultdict
class Solution:

    def __init__(self):
        self.xy = [0,0]
        self.pos = 1
        self.target = None
        #up, left,down,right
        self.directions = [(0,1),(-1,0),(0,-1),(1,0),(0,1)]
        self.value = defaultdict(int)


    def neighbors(self, x, y): 
        return ((x-1, y-1), (x, y-1), (x+1, y-1),
                (x-1, y),             (x+1, y),
                (x-1, y+1), (x, y+1), (x+1, y+1))

    def manhat_dist(self):
        man = abs(self.xy[0]) + abs(self.xy[1])
        print(man)
        return man

    def check_bounds(self, level, x, y):
        if x:
            if abs(self.xy[1] + x) > level:
                return False
        if y:
            if abs(self.xy[0] + y) > level:
                return False
        return True

    def peel_level(self, level):
        # if number equivalent to target, return
        if self.pos == self.target:
            return True
        # if new direction would be above level go to next direction
        for i in self.directions:
            # if both coords are equal to level, call new level with
            while self.check_bounds(level, i[1], i[0]):
                self.xy[0] += i[0]
                self.xy[1] += i[1]
                self.pos += 1
                # if number equivalent to target, return
                if self.pos == self.target:
                    return True
            if self.xy[0] == level and self.xy[1] == level:
                level += 1
                return self.peel_level(level)
            
    def spiral_matrix_sum(self, level):
        # if number equivalent to target, return
        # if new direction would be above level go to next direction
        for i in self.directions:
            # if both coords are equal to level, call new level with
            while self.check_bounds(level, i[1], i[0]):
                self.xy[0] += i[0]
                self.xy[1] += i[1]
                self.pos += 1
                p = (self.xy[0], self.xy[1])
                self.value[p] = sum(self.value[q] for q in self.neighbors(self.xy[0], self.xy[1])) or 1 
                print(self.value[p])
                # if number equivalent to target, return
                if self.value[p] > self.target:
                    print(self.pos)
                    print(self.value[p])
                    return True
            if self.xy[0] == level and self.xy[1] == level:
                print("next")
                level += 1
                return self.spiral_matrix_sum(level)        

    def spiral_matrix_to_n(self, target):
        self.target = target
        find = self.peel_level(1)
        if find:
            return self.manhat_dist()
    
    def spiral_matrix_to_sum(self, target):
        self.target = target
        self.value[(0,0)] = 1
        find = self.spiral_matrix_sum(1)
        if find:
            print(self.pos)
        
if __name__ == "__main__":
    s = Solution()
    #print(s.spiral_matrix_to_n(361527))
    print(s.spiral_matrix_to_sum(361527))