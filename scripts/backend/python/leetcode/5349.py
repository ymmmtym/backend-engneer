class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        l = sorted(reservedSeats)
        d = {}
        # split list exec
        for i in range(1,n+1):
            d[i] = []
            for j in l:
            if j[0] == i:
                d[i].append(j[1])
            