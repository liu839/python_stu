def reverseOnlyLetters(S: str) -> str:
    str_new=[]

    for each in S:
        if each.isalpha():
            str_new.append(each)

    str_new.reverse()

    for index,each in enumerate(S):
        if not each.isalpha():
            str_new.insert(index,each)

    return ''.join(str_new)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))