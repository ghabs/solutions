import operator


class VariableToken:
    def __init__(self, name, value=0):
        self.name = name
        self.value = int(value)

class ActionToken:
    def action_eval(self, action):
        if action == "inc":
            return operator.add
        return operator.sub

    def __init__(self, action, amount):
        self.action = self.action_eval(action)
        self.amount = int(amount)
        
    def evaluation(self, variable):
        return self.action(variable, self.amount)

class CompareToken:

    def compare_eval(self, op):
        if op == ">":
            return operator.gt
        if op == "<":
            return operator.lt
        if op == ">=":
            return operator.ge
        if op == "<=":
            return operator.le
        if op == "==":
            return operator.eq
        if op == "!=":
            return operator.ne
        raise Exception('error evaling op', op)

    def __init__(self, name, op, amount):
        self.name = name
        self.op = self.compare_eval(op)
        self.amount = int(amount)
    
    def evaluation(self, tobevar):
        #variable = eval(self.name)
        result = self.op(tobevar, self.amount)
        return result

class Solution:
    def parse(self):
        comp = []
        stack = []
        with open("data/eight.txt", 'r') as f:
            for l in f:
                "compToken, Variable, actionToken"
                line = l.split(" ")
                comp.append(line[0])
                stack.append([CompareToken(line[4], line[5], line[6]), ActionToken(line[1], line[2]), line[0]])

        return comp, stack

    def runtime(self, comp, stack):
        maxv, maxa, maxreg = None, 0, 0
        for variable in comp:
            define_stat = variable + "=0"
            exec(define_stat)
        for statement in stack:
            new_evaled_var = eval(statement[0].name)
            if statement[0].evaluation(new_evaled_var):
                action_op = statement[1].evaluation(eval(statement[2]))
                exec(statement[2] + "=" + str(action_op))
                maxreg = max(maxreg, eval(statement[2]))
        for variable in comp:
            amounteval = eval(variable)
            if amounteval > maxa:
                maxv, maxa = variable, amounteval
        return maxv


                


if __name__ == "__main__":
    v = VariableToken('a')
    line = "a dec -511 if x >= -4".split(" ")
    comp = [line[0], 'x']
    stack = []
    stack.append([CompareToken(line[4], line[5], line[6]), ActionToken(line[1], line[2]), line[0]]) 
    s = Solution()
    assert 'a' == s.runtime(comp, stack)
    stack = []
    inputa = ["b inc 5 if a > 1", "a inc 1 if b < 5", "c dec -10 if a >= 1", "c inc -20 if c == 10"]
    for l in inputa:
        line = l.split(" ")
        stack.append([CompareToken(line[4], line[5], line[6]), ActionToken(line[1], line[2]), line[0]]) 
    comp = ["b", "a", "c"]
    assert 'a' == s.runtime(comp, stack)
    comp, stack = s.parse()
    print(s.runtime(comp, stack))


