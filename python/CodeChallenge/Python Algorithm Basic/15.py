""" format

def solution(data):
    return None

data =
print(solution1(data))


위니브 회의 시간표 정렬
문제 설명
위니브 A 회의실에는 회의 시간 목록이 AM/PM 형식으로 표현되어 있습니다. 이 시간들을 24시간제로 변환한 뒤, 오름차순으로 정렬하는 코드를 작성해주세요. 시간은 'HH:MM AM' 또는 'HH:MM PM' 형식으로 주어지며, 12시간제를 24시간제로 변환할 때 '12:00 AM'은 '00:00', '12:00 PM'은 '12:00'으로 변환합니다.

제한 사항
시간은 'HH:MM AM' 또는 'HH:MM PM' 형식으로 주어집니다.
'HH'는 01에서 12 사이, 'MM'은 00에서 59 사이입니다.
시간 목록에는 최소 1개에서 최대 100개의 시간이 주어집니다.
입출력 예
 
"""


def solution(data):
    def convert_time(time):
        hh, mm, ampm = time.split(' ')[0].split(':') + time.split(' ')[1:]
        if ampm == "PM" and hh != "12":
            hh =str(int(hh) + 12)
        elif ampm =="AM" and hh =="12":
            hh = '00'
        print(f'{hh}:{mm}')
        return hh + ":"+mm

    return sorted(data, key=convert_time)


data = ["01:00 PM", "11:30 AM", "12:45 PM", "09:00 AM", "12:00 AM"]

print(solution(data))
