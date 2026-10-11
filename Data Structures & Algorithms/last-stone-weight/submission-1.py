class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first_max = -(heapq.heappop(heap))
            second_max = -(heapq.heappop(heap))
            if first_max > second_max:
                heapq.heappush(heap, -(first_max - second_max))
        return -heap[0] if heap else 0