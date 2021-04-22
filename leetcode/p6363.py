class Stu():
    def __init__(self, number, rank):
        self.number = number
        self.rank = rank
        self.avg = 0
len_students ,len_ranks = [int(i) for i in input().split(" ")]
word = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
students = []
for _ in range(len_students):
    data = input().split(" ")
    number = int(data[0])
    rank = str(data[1])
    students.append(Stu(number, rank))
score =[]
for _ in range(len_ranks):
    score.append([int(i) for i in input().split(" ")])
score = list(zip(*score))
avg_list = {}
for i in range(len_ranks):
    avg =sum(score[i])/len_ranks
    temp_list = list(filter(lambda x: abs(x - avg) <= 15, score[i]))
    avg = sum(temp_list)/len(temp_list)
    avg = int(avg+0.5)
    avg_list[word.pop(0)] = avg
for i in range(len_students):
    students[i].avg = 0.6*students[i].number + 0.4*avg_list[students[i].rank]
    students[i].avg = int(students[i].avg+0.5)
students.sort(key=lambda s:(-s.avg, s.rank))
for each in students:
    print(str(each.avg)+" "+ each.rank)
