def calculating_math_func(data, data_result, result = 1):
    if data in data_result.keys():
        result = data_result[data]
    else:
        for index in range(1, data + 1):
            result *= index
        data_result[data] = result
    result /= data ** 3
    result = result ** 10
    return result

data_result = {}
while True:
    data = int(input("Введите число: "))
    result = calculating_math_func(data, data_result)
    print(result)