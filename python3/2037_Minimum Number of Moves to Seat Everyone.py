class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        seats.sort()
        students.sort()
        for x in range(len(seats)):
            result += abs(seats[x]-students[x])
        return result