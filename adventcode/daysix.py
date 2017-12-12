import operator

class Solution:
    def redistribute(self, memory):
        #store in heap ds
        cache = dict()
        counter = 0
        memory_length = len(memory)
        i = 0
        while True:
            config = " ".join([str(x) for x in memory]) 
            if config in cache:
                return counter
            cache[config] = True            
            max_index, max_value = max(enumerate(memory), key=operator.itemgetter(1))
            i = (max_index + 1) % memory_length
            memory[max_index] = 0
            while max_value > 0:
                memory[i] += 1
                max_value -= 1
                i = (i + 1) % memory_length
            counter += 1
            #wrap around redistribute ()
            #break if heap version in cache is true

    def redistribute_cycle(self, memory):
        cache = dict()
        counter = 0
        memory_length = len(memory)
        i = 0
        while True:
            config = " ".join([str(x) for x in memory]) 
            if config in cache:
                return (counter - cache[config])
            cache[config] = counter            
            max_index, max_value = max(enumerate(memory), key=operator.itemgetter(1))
            i = (max_index + 1) % memory_length
            memory[max_index] = 0
            while max_value > 0:
                memory[i] += 1
                max_value -= 1
                i = (i + 1) % memory_length
            counter += 1       

if __name__ == "__main__":
    s = Solution()
    print(s.redistribute([0,2,7,0]))
    print(s.redistribute([2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]))
    print(s.redistribute_cycle([2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]))