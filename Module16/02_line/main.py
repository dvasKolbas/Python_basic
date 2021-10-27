first_class = list(range(160, 176, 2))
second_class = list(range(162, 180, 3))
print(first_class)
print(second_class)
first_class.extend(second_class)

for j in range(len(first_class) - 1):
  stop = True
  for i in range(len(first_class) - 1):
    if first_class[i] > first_class[i +1]:
      first_class[i], first_class[i + 1] = first_class[i + 1], first_class[i]
      stop = False
  if stop:
    break

print(first_class)