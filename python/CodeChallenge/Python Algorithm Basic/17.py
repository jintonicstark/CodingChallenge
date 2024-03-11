""" format

def solution(data):
    return None

data =
print(solution(data))

"""


def solution(data):

    all_schedules = []

    for day, dates in data.items():
        print(f"date ={day}, dates = {dates}")
        for date in dates:
            
            converted_dates = f"{date[2:]} {day}"
            print(converted_dates)
            all_schedules.append(converted_dates)

    all_schedules.sort(reverse=True)

    return all_schedules[:3]


def solution1(data):
    all_schdules = []
    for date, dates in data.items():
        
        for day in dates:
            
            all_schdules.append(f'{day[2:]} {date}')
    all_schdules.sort(reverse=True)
    return all_schdules[:3]



data = {
    "월": ["2024-01-01", "2024-01-08", "2024-01-15", "2024-01-22"],
    "화": ["2024-01-02", "2024-01-09", "2024-01-16"],
    "수": ["2024-01-03", "2024-01-10"],
    "목": ["2024-01-04", "2024-01-11", "2024-01-18"],
    "금": ["2024-01-05", "2024-01-12", "2024-01-19", "2024-01-26"],
}
print(solution1(data))
