#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

n = int(input())
leaderboard =  []
lastScore = -1
t = -1
leaderboard = list(map(int, input().rstrip().split()))
i =0 
# for i in range(0,n-1):
#     if scores[i] != scores[i+1]:
#         leaderboard.append(scores[i])
# leaderboard.append(scores[i+1])
j =0
for i in range(n-1):
    if leaderboard[i] != leaderboard[i+1]:
        leaderboard[j] = leaderboard[i]
        j+=1

leaderboard[j] = leaderboard[n-1]
leaderboard = leaderboard[0:j+1]
# print("length: ",len(leaderboard))
# print("Rewst l : ", len(set(scores)))
# print(leaderboard)
m = int(input())
alice = list(map(int, input().rstrip().split()))
flag = 0
for aliceRank in alice:
    # if aliceRank > leaderboard[0]:
    #     print("1")
    #     leaderboard.insert(0, aliceRank)
    # else:
    l = 0
    h= len(leaderboard)
    mid = -1
    while l<h:
        mid = int((h+l)/2)
        if leaderboard[mid]<= aliceRank:
            h = mid
        else:
            l = mid+1
    print(l+1)        
    # print("h: ",h) 

    # print("l: ",l) 
    # print("mid: ",mid)
    # if leaderboard[mid]==aliceRank:
    #     # flag = 1
    #     print (mid+1)
    # elif leaderboard[mid] > aliceRank:
    #     mid = mid +1
    #     leaderboard.insert(mid,aliceRank)
    #     # flag = 1
    #     print (mid+1)
    # elif leaderboard[mid] < aliceRank:
    #     leaderboard.insert(mid,aliceRank)
    #     # flag = 1
    #     print(mid+1)
        # if mid == len(leaderboard)-1 and flag == 0:
        #         leaderboard.insert(len(leaderboard),aliceRank)
        #         print(len(leaderboard))
        # else:
        #     if leaderboard[mid]!=aliceRank:
        #         if leaderboard[mid] > aliceRank:
        #             mid = mid +1
        #         leaderboard.insert(mid, aliceRank)
        #     print (mid+1)

           

    