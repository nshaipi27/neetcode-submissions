class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            stones.sort()
            first_max = stones.pop()
            second_max = stones.pop()

            if first_max > second_max:
                stones.append(first_max - second_max)
        return stones[0] if stones else 0