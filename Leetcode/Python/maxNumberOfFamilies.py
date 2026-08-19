class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)

        for row, seat in reservedSeats:
            if seat in [2, 3, 4, 5]:
                seats[row].add(0)
            if seat in [4, 5, 6, 7]:
                seats[row].add(1)
            if seat in [6, 7, 8, 9]:
                seats[row].add(2)

        res = 2 * n
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            else:
                res -= 1

        return res