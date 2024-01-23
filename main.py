import random
def menu():
    fl_for_start_alg = False
    while True:
        print("1. Заполнение матрицы вручную")
        print("2. Случайное заполнение матрицы")
        print("3. Выполнение поставлненной здачи")
        print("4. Вывод результата")
        print("5. Выход из программы")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            rows = int(input("Введите размер матрицы: "))
            matrix = []
            for i in range(rows):
                row = []
                for j in range(rows):
                    while True:
                        element = (input(f"Введите элемент [{i}][{j}]: "))
                        try:
                            element = int(element)
                            break
                        except ValueError:
                            print("Введите число")
                    row.append(element)
                matrix.append(row)
            fl_for_start_alg = True
        elif choose == "2":
            matrix = []
            rows = int(input("Введите размер матрицы: "))
            for i in range(rows):
                row = []
                for j in range(rows):
                    row.append(random.randint(1, 100))
                matrix.append(row)
            for row in matrix:
                print(row)
            fl_for_start_alg = True
        elif choose == "3":
            if not fl_for_start_alg:
                print('Отсутствуют введённые данные, сначла исполните пункты 1 или 2')
            else:
                min_value = float('inf')
                max_value = float('-inf')
                min_row = 0
                max_column = 0

                # Находим минимальный элемент и его индексы
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        if matrix[i][j] < min_value:
                            min_value = matrix[i][j]
                            min_row = i

                # Находим максимальный элемент и его индексы
                for j in range(len(matrix[0])):
                    for i in range(len(matrix)):
                        if matrix[i][j] > max_value:
                            max_value = matrix[i][j]
                            max_column = j

                # Заменяем строку с минимальным элементом на столбец с максимальным элементом
                for i in range(len(matrix)):
                    matrix[i][max_column], matrix[min_row][i] = matrix[min_row][i], matrix[i][max_column]
        elif choose == "4":
            try:
                for rows in matrix:
                    print(rows)
            except:
                print("Создайте матрицу")
        elif choose == "5":
            break
        else:
            print("Данный пункт отсутствует в меню")


if __name__ == "__main__":
    menu()
