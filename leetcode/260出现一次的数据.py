def singleNumber(self, nums: List[int]) -> List[int]:
    dict_={}
    list_=[]
    for each in nums:
        try:
            dict_[each]+=1
        except KeyError:
            dict_[each]=1
    for each in dict_:
        if dict_[each]==1:
            list_.append(each)
            if len(list_)==2:
                break
    return list_