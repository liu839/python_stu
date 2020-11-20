class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        print(people)
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res