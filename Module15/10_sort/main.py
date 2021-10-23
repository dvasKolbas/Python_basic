N = [1, 5, 2, 10, 7, 9]
count = 0
for j in range(len(N) - 1):
  count +=1
  stop = True
  for i in range(len(N) - 1):
    if N[i] > N[i +1]:
      N[i], N[i + 1] = N[i + 1], N[i]
      stop = False
  if stop:
    break
print(count)
print(N)