from typing import List
# In this problem I used a dictionary to count all the elements frequency
# then simply sorted in reverse order using the sort function and then displayed the returned the total number of top k frequent elements
def topK(nums:List[int], k:int) -> List[int]:
    rl = []
    e = list(set(nums))
    c = [0]*len(e)
    d = dict(zip(e,c))
    for i in nums:
        d[i] += 1
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    keys = list(d.keys())
    for i in range(k):
        rl.append(keys[i])
    return rl
# This is a faster method, it uses bucket sort to shorten the time it needs to create the required buckets with the count of the various elements
# then just traverse through the list backwards to get the required result
def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num,cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topK(nums,k))
