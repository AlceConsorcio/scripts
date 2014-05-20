import datetime
prev = 6
counter = 0
wof = 0
date = datetime.date(2014, 06, 1)
for i in range(30):
    if prev == date.isocalendar()[1]:
        print date, " ", date.month, " ", date.isocalendar()[1], " ", date.isocalendar()[2]
        date += datetime.timedelta(days=1)
        counter += 1
        if counter == 6:
            counter = 0
            wof += 1
            print "%s"%wof
    else:
        prev = date.isocalendar()[1]
        print "------------------------------------"
        print date, " ", date.month, " ", date.isocalendar()[1], " ", date.isocalendar()[2]
        date += datetime.timedelta(days=1)
if counter < 6:
    print wof+1
