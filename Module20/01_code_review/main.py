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


def find_intersts(students):
    interests_lst = []
    surname_lenth = ''
    for i_id, i_info in students.items():
        #lst += (dict[i]['interests'])
        if "interests" in i_info:
            interests_lst += (i_info["interests"])
        if "surname" in i_info:
            surname_lenth += i_info['surname']
    #cnt = 0
    # for s in string:
    #     cnt += 1
    return interests_lst, len(surname_lenth)


#pairs = []
print("ID и возраст:")
for i_id, i_info in students.items():
    #pairs += (i, students[i]['age'])
    if "age" in i_info:
        print(i_id, i_info["age"])
print()

interests_lst, surname_lenth = find_intersts(students)
#l = f(students)[1]
print("Интересы:", ", ".join(interests_lst))
print("\nДлина фамилий:", surname_lenth)
# TODO исправить код
