import datetime

def militaryTimeNow():
    return datetime.datetime.utcnow().isoformat()[:-3]+'Z'


def militaryTimeToDatetime(time):
    """2018-05-16T10:16:24.666Z"""
    date = time.split("T")[0].split("-")

    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    rest = time.split("T")[1]
    hour= int(rest.split(":")[0])
    minute= int(rest.split(":")[1])
    second= int(rest.split(":")[2].split(".")[0])
    return datetime.datetime(year,month,day,hour,minute,second)


def compareMilitaryTime(endTime,startTime):
    """returns difference in seconds between 2 military times"""
    return militaryTimeToDatetime(endTime)-militaryTimeToDatetime(startTime)
