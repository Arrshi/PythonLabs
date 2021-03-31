from datetime import datetime, time, timedelta

arr = [int(i) for i in input().split(':')]
arr2 = [int(i) for i in input().split(':')]

firstTime = datetime.combine(datetime.min, time(arr[0], arr[1]))
secondTime = datetime.combine(datetime.min, time(arr2[0], arr2[1]))

subtrct = firstTime - secondTime

if subtrct > timedelta(0, 15):
    print("hello")