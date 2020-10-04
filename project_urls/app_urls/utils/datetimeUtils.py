import datetime

def militaryTimeNow():
    return datetime.datetime.utcnow().isoformat()[:-3]+'Z'