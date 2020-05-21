def isUnique(astr: str) -> bool:
    for i,each in enumerate(astr):
        if each in (astr[:i]+astr[i+1:]):
            return False
    return True
    #        return len(astr)==len(set(astr))
print(isUnique("abcddc"))