strs =["car","racecar","cary"]

class Solution:
    def __init__(self, strs: list[str]) -> None:
        self.strs = strs

    @staticmethod
    def llc(s1, s2):
        if len(s1) <= 1:
            if s1 in s2:
                return s1
            return ""
        
        indexs = []
        for i in range(len(s1)-1):
            if s1[i] + s1[i+1] in s2:
                indexs.append(i)
                indexs.append(i+1)
                    
        indexs = set(indexs)

        if len(indexs) == 0:
            for c in s1:
                if c in s2: return c

        return ''.join(s1[i] for i in indexs)


    def solve(self):
        self.strs.sort(key=len)

        substring = self.strs[0]
        if len(substring) < 0:
            return ""
        
        for w in self.strs[1:]:
            res = self.llc(substring, w)
            substring = res
        return substring
    
result = Solution(strs) 
print(result.solve())

# Thanh A code
print("Hello Thanh B")