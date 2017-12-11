class Solution:
    def create_stack(self):
        with open("data/five.txt", 'r') as f:
            st = f.read().splitlines()
            st = map(int, st)
            return st

    def traverse_stack(self, stack):
        sHeight = len(stack)
        i, counter = 0, 0
        while i < sHeight:
            tmp = stack[i]
            stack[i] += 1
            counter += 1
            i += tmp
        return counter

    def traverse_input(self):
        stack = self.create_stack()
        return self.traverse_stack(stack)

    def traverse_stack_two(self, stack):
        sHeight = len(stack)
        i, counter = 0, 0
        while i < sHeight:
            tmp = stack[i]
            if stack[i] >= 3:
                stack[i] -= 1
            else:
                stack[i] += 1
            counter += 1
            i += tmp
        return counter        

    def traverse_input_two(self):
        stack = self.create_stack()
        return self.traverse_stack_two(stack)



if __name__ == "__main__":
    s = Solution()
    assert 5 == s.traverse_stack([0, 3, 0, 1, -3])
    print(s.traverse_input())
    print(s.traverse_input_two())