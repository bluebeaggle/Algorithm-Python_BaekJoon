import sys

n = int(sys.stdin.readline())
exam = list(map(int,sys.stdin.readline().split()))
Average_exam = list(map(lambda x: (x/max(exam))*100, exam))

print(sum(Average_exam)/n)