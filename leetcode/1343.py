def numOfSubarrays(arr, k, threshold ) -> int:
    res = []

    def solv(temp, nums):
        nonlocal k,res,threshold
        
        if len(temp) == k:
            if sum(temp) / k > threshold:
                res.append(temp)
            return
        else:
            for i, num in enumerate(nums):
                solv(temp+[num], nums[:i]+nums[i+1:])
    solv([], arr)

    return len(res) 
    

print (numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
