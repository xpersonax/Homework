import datetime

def get_days_from_today(date): 
    try:
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    today = datetime.datetime.today()
    difference = today - parsed_date
    return difference.days

result = get_days_from_today("2021-10-09")
print(result)

result = get_days_from_today("не дата")
print(result)