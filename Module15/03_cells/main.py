def input_cells(count, cells):
    for i in range(count):
        cells.append(int(input("Эффективность " + str(i + 1) + " клетки: ")))
    return cells


def print_cells(cells):
    print("\nНеподходящие значения:", end=" ")
    for i in range(len(cells)):
        if cells[i] < i:
            print(cells[i], end=" ")


count = int(input("Введите кол-во клеток: "))
cells = []
cells = input_cells(count, cells)
print_cells(cells)