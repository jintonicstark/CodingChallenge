""" format

def solution(data):
    return None

data =
print(solution(data))

"""


def solution(data):
    def convert_date(date):

        if "-" in date:
            day, month, year = date.split("-")
        elif "/" in date:
            month, day, year = date.split("/")
        else:
            year, day, month = date.split(".")

        return year, month, day

    convert_dates = [convert_date(date) for date in data]
    sorted_datas = sorted(convert_dates)

    return ["/".join(date) for date in sorted_datas]

def solution1(data):
    def convert_date(date):
        if "-" in date:
            day, month, year = date.split("-")
        elif "/" in date:
            month, day, year = date.split("/")
        else:
            year, day, month = date.split(".")

        return year, month, day

    convert_dates = [convert_date(date) for date in data]
    sorted_dates = sorted(convert_dates)         
    return ["/".join(data) for data in sorted_dates]


data = ["20-01-2024", "12/15/2023", "2022.05.30"]

print(solution1(data))
