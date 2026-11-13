class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for ui, vi, ti in times:
            adj_list[ui].append((vi, ti))
        
        min_heap = [(0, k)]
        visited = set()
        total_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_time = time

            for neighbor, ti in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (ti + time, neighbor))

        return total_time if len(visited) == n else -1

