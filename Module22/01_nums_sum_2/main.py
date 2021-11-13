num_file = open("numbers.txt", "r")
num = [int(i) for i in num_file.read().split()]
num_file.close()
sum_file = open("answer.txt", "w")
sum_file.write(str(sum(num)))
sum_file.close()
