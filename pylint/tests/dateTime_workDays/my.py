import calendar
from datetime import timedelta
from datetime import datetime


def formatDate(date):
    return f"{date.day}.{date.month}.{date.year}"


def incrementMonth(when):
    days = calendar.monthrange(when.year, when.month)[1]
    return when + timedelta(days=days)


if __name__ == "__main__":
    currentDate = datetime(*list(map(int, input().split(".")))[::-1])
    afterAMonth = incrementMonth(currentDate)
    print(formatDate(currentDate))

    tmpDate = currentDate + timedelta(days=4)
    while afterAMonth > tmpDate:
        if tmpDate.weekday() == 6:
            tmpDate = tmpDate + timedelta(days=1)
        print(formatDate(tmpDate))
        tmpDate = tmpDate + timedelta(days=4)

