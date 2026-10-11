class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            dist_x = (0 - point[0])**2
            dist_y = (0 - point[1])**2
            distances.append((math.sqrt(dist_x+dist_y), point))
        
        heapq.heapify(distances)
        ans = []
        
        while len(ans) < k:
            val, pos = heapq.heappop(distances)
            ans.append(pos)
        return ans

        