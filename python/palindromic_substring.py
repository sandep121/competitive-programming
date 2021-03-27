class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i, v in enumerate(s):
            result+=1
            #             check for same char string
            for j in range(i+1, len(s)):
                if v == s[j]:
                    result+=1
                    k=i-1
                    l=j+1
                    if s[k] != v:
                        while k>=0 and l < len(s):
                            if s[k] == s[l]:
                                print(k.__str__()+" "+l.__str__())
                                result += 1
                            else:
                                break
                            k-=1
                            l+=1
                else:
                    break
            k=i-1
            l=i+1
            if s[k] != v:
                while k>=0 and l < len(s):
                    if s[k] == s[l]:
                        print(k.__str__()+" "+l.__str__())
                        result += 1
                    else:
                        break
                    k-=1
                    l+=1
        return result

print(Solution().countSubstrings("leetcode"))
