from datetime import datetime


def dt_from_str(str):  # input example: "2020-02-05 16:20:00"
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
