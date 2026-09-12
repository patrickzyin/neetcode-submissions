class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-stone for stone in stones]
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            largest = -heapq.heappop(self.maxHeap)
            secondLargest = -heapq.heappop(self.maxHeap)
            stone = largest - secondLargest
            heapq.heappush(self.maxHeap, -(stone))
        return -self.maxHeap[0]

        