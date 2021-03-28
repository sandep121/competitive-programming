class Solution:
    def __init__(self):
        self.alpha = [0]*26
        self.count = [0]*10
    def pop_alpha(self, str):
        min = 50000
        for i in str:
            if self.alpha[ord(i)-ord('a')]<min:
                min = self.alpha[ord(i)-ord('a')]
        for i in str:
            self.alpha[ord(i)-ord('a')]-=min
        return min
    def originalDigits(self, s: str) -> str:
        for i in s:
            self.alpha[ord(i)-ord('a')]+=1
        counting={0:"zero",2:"two",4:"four",6:"six",8:"eight",1:"one",3:"three",5:"five",7:"seven",9:"nine"}
        for i,v in counting.items():
            self.count[i]=self.pop_alpha(v)
        result = ""
        for i, v in enumerate(self.count):
            result+=str(str(i)*v)
        return result

print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))
