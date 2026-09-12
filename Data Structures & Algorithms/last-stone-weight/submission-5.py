class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-stone for stone in stones]
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            largest = heapq.heappop(self.maxHeap)
            secondLargest = heapq.heappop(self.maxHeap)
            if secondLargest > largest:
                stone = largest - secondLargest    
                heapq.heappush(self.maxHeap, stone)
        heapq.heappush(self.maxHeap, 0)
        return abs(self.maxHeap[0])

        