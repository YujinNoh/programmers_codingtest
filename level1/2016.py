def solution(a, b):
    year2016 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = (0 if a == 1 else sum(year2016[0 : a - 1])) + b

    return week[days % 7]
