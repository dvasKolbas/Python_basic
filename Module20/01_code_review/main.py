students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i_id, i_info in dict.items():
        #lst += (dict[i]['interests'])
        if "interests" in i_info:
            lst += (i_info["interests"])
        if "surname" in i_info:
            string += i_info['surname']
    #cnt = 0
    # for s in string:
    #     cnt += 1
    return lst, len(string)


#pairs = []
print("ID и возраст:")
for i_id, i_info in students.items():
    #pairs += (i, students[i]['age'])
    if "age" in i_info:
        print(i_id, i_info["age"])
print()

my_lst, l = f(students)
#l = f(students)[1]
print("Интересы:", ", ".join(my_lst))
print("\nДлина фамилий:", l)
# TODO исправить код
