from datetime import date


def datetime_from_string(input_date: str):
    split = input_date.split("/")
    print(split)
    date_object = date(int(split[2]), int(split[0]), int(split[1]))
    return date_object


def isMerchantNamePartialMatch(name1: str, name2: str):
    if name1 == name2:
        return False
    return True
