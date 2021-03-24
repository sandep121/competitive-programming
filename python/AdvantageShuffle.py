from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort(reverse=True)
        C = [(v, i) for i, v in enumerate(B)]
        C.sort(reverse=True)
        result = [None]*len(A)
        A_l = len(A)-1
        A_i = 0
        for t in C:
            v,i = t
            if v < A[A_i]:
                result[i]=A[A_i]
                A_i+=1
            else:
                result[i]=A[A_l]
                A_l-=1
        return result


print(Solution().advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]))
