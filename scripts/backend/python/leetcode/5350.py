import numpy as np

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        lohi = [i for i in range(lo,hi+1)]
        l = []
        for i in lohi:
            cnt = 0
            while i == 1:
                cnt += 1
                if i % 2 == 0:
                    i //= 2
                else:
                    i = 3*i + 1
            print(cnt)
            l.append(cnt)
        # print(l)
        rank = np.array(l).argsort().tolist()
        # print(rank)
        index = rank.index(k-1)
        return lohi[index]