class Solution:

    def read_stream(self, input=None):
        ignf = garf = False
        level = groups = score = garc = 0

        if not input:
            with open("data/nine.txt", 'r') as f:
                while True:
                    c = f.read(1)
                    if not c:
                        break
                    if ignf:
                        ignf = False
                    else:
                        if c == '!':
                            ignf = True
                        elif garf:
                            if c == '>':
                                garc = False
                            else:
                                count += 1
                        else:
                            if c == '<':
                                garf = True
                            elif c == '{':
                                level += 1
                            elif c == '}':
                                score += level
                                groups += 1
                                level -= 1
                            else:
                                pass
        return score, garc

if __name__ == "__main__":
    s = Solution()
    print(s.read_stream())
                                
