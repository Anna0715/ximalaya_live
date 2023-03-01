import datetime
import time

timestamp=int(round(time.time()*1000))
startime = timestamp - timestamp % (10 * 60) + (10 * 60)
endtime = timestamp - timestamp % ((20) * 60) + ((20) * 60)
print(startime,endtime)
m=(datetime.datetime.now()+datetime.timedelta(minutes=20)).strftime("%Y-%m-%d %H:%M:%S")
s=int(round(time.mktime(time.strptime(m,'%Y-%m-%d %H:%M:%S'))*1000))
print(m,s,(datetime.datetime.now()+datetime.timedelta(minutes=20)))
print(type(datetime.datetime.now().month))
startAt=(datetime.datetime.now()+datetime.timedelta(minutes=20)).strftime("%Y-%m-%d %H:%M:%S")
endAt=(datetime.datetime.now()+datetime.timedelta(minutes=50)).strftime("%Y-%m-%d %H:%M:%S")
startime = int(round(time.mktime(time.strptime(startAt, '%Y-%m-%d %H:%M:%S')) * 1000))
print(startime)
