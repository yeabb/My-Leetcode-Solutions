class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        arr = [[] for i in range(len(nums)+1)]
        for key, val in count.items():
            arr[val].append(key)
        output = []
        for i in range(len(nums), 0, -1):
            if arr[i] != []:
                for j in range(len(arr[i])):
                    output.append(arr[i][j])
                    k -= 1
            if k == 0:
                return output
        