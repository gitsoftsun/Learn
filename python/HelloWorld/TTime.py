#encoding=utf-8
#Test Time
import time
ticks = time.time()
print "number of ticks since 12:00am, January 1, 1970: ", ticks
localTime = time.localtime(time.time())
print "local current time :", localTime
# print "local year %s- month %s - day %s - hour %s - minutes %s - seconds %s -week %s " %(localTime.tm_year, localTime.tm_mon, localTime.tm_mday, localTime.tm_hour, localTime.tm_min, localTime.tm_sec, localTime.tm_wday, localTime.tm_yday)	
print "tm_year=%s, tm_mon=%s, tm_mday=%s, tm_hour=20, tm_min=4, tm_sec=27, tm_wday=4, tm_yday=16, tm_isdst=0" %(localTime.tm_year, localTime.tm_mon, localTime.tm_yday)
#格式化时间
print "Current time is : ", time.asctime(time.localtime(time.time()))
import calendar
print calendar.month(2015, 1)