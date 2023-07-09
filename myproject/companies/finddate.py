import datetime


def finddate(year, period):
    deadline = None
    year = int(year)

    if period == 'january':
        deadline = datetime.datetime(year, 2, 25)
    elif period == 'february':
        deadline = datetime.datetime(year, 3, 25)
    elif period == 'march' or period == '1st quarter':
        deadline = datetime.datetime(year, 4, 25)
    elif period == 'april':
        deadline = datetime.datetime(year, 5, 25)
    elif period == 'may':
        deadline = datetime.datetime(year, 6, 25)
    elif period == 'june' or period == '2nd quarter':
        deadline = datetime.datetime(year, 7, 25)
    elif period == 'july':
        deadline = datetime.datetime(year, 8, 25)
    elif period == 'august':
        deadline = datetime.datetime(year, 9, 25)
    elif period == 'september' or period == '3rd quarter':
        deadline = datetime.datetime(year, 10, 25)
    elif period == 'october':
        deadline = datetime.datetime(year, 11, 25)
    elif period == 'november':
        deadline = datetime.datetime(year, 12, 25)
    elif period == 'december' or period == '4th quarter':
        deadline = datetime.datetime(year+1, 1, 25)

    if deadline.weekday() == 5:
        deadline += datetime.timedelta(days=2)
    if deadline.weekday() == 6:
        deadline += datetime.timedelta(days=1)

    return deadline

