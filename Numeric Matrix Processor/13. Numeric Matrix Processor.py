while True:
    matrix_1 = []
    matrix_2 = []
    sum_mat = []

    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")

    def main_dia_transpose(matrix):
        transposed_mat = []
        for i in range(len(matrix)):
            lt = [matrix[j][i] for j in range(len(matrix[0]))]
            transposed_mat.append(lt)
        return transposed_mat

    def minor(matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

    def determinant(matrix):
        det = 0
        if len(matrix) == 1 and len(matrix[0]) == 1:
            det = matrix[0][0]
        elif len(matrix) == 2 and len(matrix[0]) == 2:
            det += matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            for x in range(len(matrix[0])):
                det += ((-1) ** (x + 1 + 1)) * matrix[0][x] * determinant(minor(matrix, 0, x))
        return det

    choice = input("Your choice: ")

    if choice == "0":
        quit()

    elif choice == "1":
        row_1, col_1 = map(int, input("Enter size of first matrix: ").split())
        print("Enter first matrix:")
        for i in range(row_1):
            row = input().split()
            matrix_1.append([float(i) for i in row])

        row_2, col_2 = map(int, input("Enter size of second matrix: ").split())
        print("Enter second matrix:")
        for i in range(row_2):
            row = input().split()
            matrix_2.append([float(i) for i in row])

        if row_1 == row_2 and col_1 == col_2:
            for i in range(row_1):
                lt = [x + y for x, y in zip(matrix_1[i], matrix_2[i])]
                sum_mat.append(lt)

            print("The result is:")
            for i in range(len(sum_mat)):
                print(" ".join([str(j) for j in sum_mat[i]]))
        else:
            print("The operation cannot be performed.")

    elif choice == "2":
        row_1, col_1 = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        for i in range(row_1):
            row = input().split()
            matrix_1.append([float(i) for i in row])

        constant = float(input("Enter constant: "))

        print("The result is:")
        for i in range(row_1):
            lt = [constant * x for x in matrix_1[i]]
            sum_mat.append(lt)
            print(" ".join([str(j) for j in sum_mat[i]]))

    elif choice == "3":
        row_1, col_1 = map(int, input("Enter size of first matrix: ").split())
        print("Enter first matrix:")
        for i in range(row_1):
            row = input().split()
            matrix_1.append([float(i) for i in row])

        row_2, col_2 = map(int, input("Enter size of second matrix: ").split())
        print("Enter second matrix:")
        for i in range(row_2):
            row = input().split()
            matrix_2.append([float(i) for i in row])

        if row_2 == col_1:
            t_matrix_2 = []
            for i in range(col_2):
                lt = [matrix_2[j][i] for j in range(row_2)]
                t_matrix_2.append(lt)

            for i in range(row_1):
                lt2 = [sum((x * y for x, y in zip(matrix_1[i], t_matrix_2[j]))) for j in range(len(t_matrix_2))]
                sum_mat.append(lt2)

            print("The result is:")
            for i in range(len(sum_mat)):
                print(" ".join([str(j) for j in sum_mat[i]]))

        else:
            print("The operation cannot be performed.")

    elif choice == "4":
        print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        transpose_choice = input("Your choice: ")
        if transpose_choice == "1":
            row_1, col_1 = map(int, input("Enter matrix size: ").split())
            print("Enter matrix: ")
            for i in range(row_1):
                row = input().split()
                matrix_1.append([float(i) for i in row])

            for i in range(col_1):
                lt = [matrix_1[j][i] for j in range(row_1)]
                sum_mat.append(lt)

            print("The result is:")
            for i in range(len(sum_mat)):
                print(" ".join([str(j) for j in sum_mat[i]]))

        elif transpose_choice == "2":
            row_1, col_1 = map(int, input("Enter matrix size: ").split())
            print("Enter matrix: ")
            for i in range(row_1):
                row = input().split()
                matrix_1.append([float(i) for i in row])

            for i in range(col_1):
                lt = [matrix_1[j][i] for j in range(row_1)]
                sum_mat.append(lt[::-1])
            sum_mat = sum_mat[::-1]

            print("The result is:")
            for i in range(len(sum_mat)):
                print(" ".join([str(j) for j in sum_mat[i]]))

        elif transpose_choice == "3":
            row_1, col_1 = map(int, input("Enter matrix size: ").split())
            print("Enter matrix: ")
            for i in range(row_1):
                row = input().split()
                sum_mat.append([float(i) for i in row][::-1])

            print("The result is:")
            for i in range(len(sum_mat)):
                print(" ".join([str(j) for j in sum_mat[i]]))

        elif transpose_choice == "4":
            row_1, col_1 = map(int, input("Enter matrix size: ").split())
            print("Enter matrix: ")
            for i in range(row_1):
                row = input().split()
                sum_mat.append([float(i) for i in row])
            sum_mat = sum_mat[::-1]

            print("The result is:")
            for i in range(len(sum_mat)):
                print(" ".join([str(j) for j in sum_mat[i]]))

    elif choice == "5":
        row_1, col_1 = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        for i in range(row_1):
            row = input().split()
            matrix_1.append([float(i) for i in row])

        print(f"The result is:\n{determinant(matrix_1)}")

    elif choice == "6":
        row_1, col_1 = map(int, input("Enter size of matrix: ").split())
        print("Enter matrix:")
        for i in range(row_1):
            row = input().split()
            matrix_1.append([float(i) for i in row])

        if determinant(matrix_1) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            cofactor_matrix_1 = []
            for i in range(row_1):
                cofactor_matrix_1.append([((-1) ** (i + j + 2)) * determinant(minor(matrix_1, i, j)) for j in range(col_1)])

            transposed = main_dia_transpose(cofactor_matrix_1)
            det = determinant(matrix_1)

            inverse_matrix = []
            for i in range(len(transposed)):
                inverse_matrix.append([(transposed[i][j] / det) for j in range(len(transposed[0]))])

            print("The result is:")
            for i in range(len(inverse_matrix)):
                print(" ".join([str(int(j)) if j == 0.0 or j == -0.0 else str(int(j * 100) / 100) for j in inverse_matrix[i]]))
