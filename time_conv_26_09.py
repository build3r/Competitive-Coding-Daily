#https://www.hackerrank.com/challenges/time-conversion/problem
import datetime
if __name__ == '__main__':
    s = input()
    tm = datetime.datetime.strptime(s,"%I:%M:%S%p").time()
    print(tm.strftime('%H:%M:%S'))
    #test