class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # is a hashmap for number of times each number appears 
        freq = [[] for i in range(len(nums)+1)] # creates buckets (each bucket of index n possesses numbers that appeared n times)

        # adds to count where key is current iterated number & value is its frequency
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        # adds num (frequency) to the bucket corresponding to index cnt
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res