from typing import List
# In this problem I used a dictionary to count all the elements frequency
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

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topK(nums,k))
