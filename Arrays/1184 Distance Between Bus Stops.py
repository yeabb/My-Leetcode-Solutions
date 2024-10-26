class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        if start > destination:
            temp = start
            start = destination
            destination = temp

        n = len(distance)
        clockwiseDistance = sum(distance[start:destination])
        antiClockwiseDistance = sum(distance[0:start]) + sum (distance[destination:n+1])
        return min (clockwiseDistance, antiClockwiseDistance)

        

