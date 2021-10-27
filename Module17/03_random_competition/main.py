import random
team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team3 = [max(team1[i], team2[i]) for i in range(20)]
print("Первая команда:",team1)
print("\nВторая команда:",team2)
print("\nПобедители тура:",team3)