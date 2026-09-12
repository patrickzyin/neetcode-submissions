class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            return math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)

        res = []
        minHeap = [(distance(point), point) for point in points]
        heapq.heapify(minHeap)
        for i in range(k):
            dist, point = heapq.heappop(minHeap)
            res.append(point)
        return res


        