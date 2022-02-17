# 2884번 알람 시계

hour, minute = map(int, input().split())
hour = int(hour)
minute = int(minute)
change_hour = hour
change_minute = minute - 45

if change_minute < 0:
    change_minute = 60 + change_minute
    change_hour -= 1
if change_hour < 0 :
    change_hour = 23
if change_hour >= 24:
    hour = 0

print(change_hour)
print(change_minute)
