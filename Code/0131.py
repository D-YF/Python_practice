from typing import List, Optional

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill==5: five += 1

            elif bill==10:
                if five<=0: return False
                ten += 1
                five -= 1
            
            else: #bill==20
                if ten>=1 and five>=1:
                    ten -= 1
                    five -= 1
                elif five>=3:
                    five -= 3
                else:
                    return False
        
        return True


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # First srot based on x[0] in descent order, if it's same, try x[1]
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []

        for p in people:
            queue.insert(p[1], p)

        return queue        

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0: return 0
        points.sort(key=lambda x:x[0])

        ans = 1
        for i in range(1, len(points)):
            if points[i][0]>points[i-1][1]:
                ans += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])
        
        return ans

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x: (x[0],x[1]))

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                ans += 1
                intervals[i][1] = intervals[i-1][1]
        return ans