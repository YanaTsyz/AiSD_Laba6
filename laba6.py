import random
import time
import numpy as np

def print_matrix(M, matr_name, tt):
    print("Матрица " + matr_name + ", промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:                       # делаем перебор всех строк матрицы
        for j in i:                   # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

print("\n---------- Результат работы программы ----------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100 : "))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число.\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100 : "))
    K = int(input("Введите число К = "))
    start = time.time()
    A, F, AF, FT = [], [], [], []                 # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        FT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):                        # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    
    for i in range(row_q):                        # формируем матрицу F, копируя из матрицы А
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []                                        # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):                         # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[size + row_q % 2 + i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)

    

    quantity = 0                                  # считаем количетво нулей по периметру
    multiplication = 1                            # считаем произведение чисел по периметру
    for i in range (size): 
        for j in range (size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                multiplication *= C[i][j]
                if C[i][j] == 0:
                    quantity += 1

    if quantity > multiplication:
        print("Случай 1.")
        for i in range(size + row_q % 2, row_q):                          # меняем подматрицы C и E местами симметрично
            for j in range(size + row_q % 2, row_q):
                variable = F [i][j]
                F [i][j] = F[i-size + row_q % 2][j-size + row_q % 2]
                F[i-size + row_q % 2][j-size + row_q % 2] = variable

    else:
        print("Случай 2.")
        for i in range(0, size + row_q % 2):                              # меняем подматрицы C и B местами несимметрично
            for j in range(size + row_q % 2, row_q): 
                variable = F [i][j]
                F [i][j] = F[i + size + row_q % 2][j]
                F[i + size + row_q % 2][j] = variable
                

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    sum_diagonal = 0

    for i in range(row_q):                                                # сумма диагональных элементов матрицы F                       
        for j in range(row_q):
            if i == j:
                sum_diagonal = sum_diagonal + F[i][j] + F[i][row_q - 1 - j]
        
    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("Матрицы A или F вычислить нельзя.")
    elif np.linalg.det(A) > sum_diagonal:
        A = ((np.dot(np.linalg.matrix_power(A, -1), np.transpose(A))) - (np.dot(K, F)))
        finish = time.time()
    else:
        A = np.dot((A + np.tril(A) - np.linalg.matrix_power(F, -1)), K)
        finish = time.time()
        
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    print(f"Время работы программы {time.time()-start}.")

    """"""""""""""""""""""""""""""""""""""""""""""""""""""
    
    from matplotlib import pyplot as plt
    import matplotlib.cm as cm
    import seaborn as sns
    import pandas as pd

    """"""""""""""""""""""""""""""""""""""""""""""""""""""        

    plt.title("Plot", fontsize=15)                                 # 1 пример (matplotlib)
    plt.xlabel("Number", fontsize=13)
    plt.ylabel("Resalt", fontsize=13)
    
    for j in range (row_q):                                           
        plt.plot([i for i in range(row_q)], A[j][::], marker='x') 
    plt.show()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""

    sns.set_theme(style="white")                                   # 2 пример (seaborn)
    uniform_data = A
    if row_q >= 50 or K >= 10:
        graph = sns.heatmap(A, vmin=-20 * row_q, vmax=20 * row_q)
    elif row_q < 50 or K < 10:
        graph = sns.heatmap(A, vmin=-50, vmax=50, annot_kws={'size': 7}, annot=True, fmt=".1f")
    plt.show()
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""

    plt.title("Pie", fontsize=15)                                 # 3 пример (matplotlib)
    plt.xlabel("Number", fontsize=13)
    plt.ylabel("Resalt", fontsize=13)
    
    for j in range(row_q):
        plt.pie([i for i in range(row_q)])
    plt.show()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""

    df = pd.DataFrame(A)                                          # 4 пример (seaborn)
    p = sns.lineplot(data=df)                                     
    p.set_xlabel("Номер элемента в столбце", fontsize=15)
    p.set_ylabel("Значение", fontsize=15)
    plt.show()
    
except ValueError:
   print("\nЭто не число.")

