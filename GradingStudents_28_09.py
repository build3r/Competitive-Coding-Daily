#https://www.hackerrank.com/challenges/grading/problem
n = int(input())
for i in range(n):
    og = int(input())
    if (og < 38):
        print(og)
    else:
        x = og % 5
        if(x < 3):
            print(og)
        else:
            print(og+(5-x))

