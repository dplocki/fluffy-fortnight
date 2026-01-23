class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        removed = set()
        previous_nodes = [i-1 for i in range(n)]
        next_nodes = [i+1 for i in range(n)]
        next_nodes[-1] = -1

        pair_sums = [(nums[i] + nums[i + 1], i) for i in range(n - 1)]
        heapq.heapify(pair_sums)

        bad = sum(1 for a, b in pairwise(nums) if a > b)
        result = 0

        while bad > 0 and n > 1:
            pair_sum, first_index = heapq.heappop(pair_sums)
            second_index = next_nodes[first_index]
            if first_index in removed or second_index == -1:
                continue

            if second_index in removed or nums[first_index] + nums[second_index] != pair_sum:
                continue

            pair_prev_index = previous_nodes[first_index]
            pair_next_index = next_nodes[second_index]

            if pair_prev_index != -1 and nums[pair_prev_index] > nums[first_index]:
                bad -= 1

            if nums[first_index] > nums[second_index]:
                bad -= 1

            if pair_next_index != -1 and nums[second_index] > nums[pair_next_index]:
                bad -= 1

            removed.add(second_index)
            nums[first_index] = pair_sum
            next_nodes[first_index] = pair_next_index
            if pair_next_index != -1:
                previous_nodes[pair_next_index] = first_index

            if pair_prev_index != -1 and nums[pair_prev_index] > pair_sum:
                bad += 1

            if pair_next_index != -1 and pair_sum > nums[pair_next_index]:
                bad += 1

            n -= 1
            result += 1

            if pair_prev_index != -1:
                heapq.heappush(pair_sums, (nums[pair_prev_index] + pair_sum, pair_prev_index))

            if pair_next_index != -1:
                heapq.heappush(pair_sums, (pair_sum + nums[pair_next_index], first_index))

        return result
