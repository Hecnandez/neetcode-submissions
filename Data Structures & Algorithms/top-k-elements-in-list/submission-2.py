class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {} # num: frequency
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        print(frequencies)
        top = sorted(frequencies.values(), reverse = True)
        res = []
        for i in range(k):
            print(top)
            key = next((k for k, v in frequencies.items() if v == top[i]), None)
            res.append(key)
            frequencies.pop(key)
        return res