import re
from typing import List


def check_numbers(nums: List) -> None:
    sample = r"\b[8,9]\d{9}\b"
    res = []
    for id, num in enumerate(nums):
        print(id + 1, end=" номер: ")
        if re.match(sample, num):
            print("всё в порядке")
        else:
            print("не подходит")
    return




numbers = ['9999999999', '999999-999', '99999x9999']
check_numbers(numbers)
