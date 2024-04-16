####    时间函数
    from PyQt6.QtCore import QDate,QTime,QDateTime,Qt
    now=QDate.currentDate()
    print(now.toString(Qt.DateFormat.ISODate))
    #2024-04-10
    print(now.toString(Qt.DateFormat.RFC2822Date))#10 Apr 2024
    datetime=QDateTime.currentDateTime()
    print(datetime.toString())#Wed Apr 10 14:38:17 2024
    time=QTime.currentTime()
    print(time.toString(Qt.DateFormat.ISODate))#14:38:17
    print("local datetime:",datetime.toString(Qt.DateFormat.ISODate))#local datetime: 2024-04-10T14:41:25
    print('Universal datetime: ', datetime.toUTC().toString(Qt.DateFormat.ISODate))#Universal datetime:  2024-04-10T06:42:22Z
    print(f'The offset from UTC is: {datetime.offsetFromUtc()} seconds') #The offset from UTC is: 28800 seconds
    d=QDate(1945,5,7)
    print(f'Days in month: {d.daysInMonth()}')#Days in month: 31
    print(f'Days in year: {d.daysInYear()}')#Days in year: 365
####
