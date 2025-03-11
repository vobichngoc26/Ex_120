import numpy as np

def create_random_matrix(N, M):
    return np.random.randint(-100, 101, (N, M))

def calculate_determinant(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        return np.linalg.det(matrix)
    else:
        return "Determinant is only defined for square matrices."

def find_inverse(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            return "Matrix is singular and cannot be inverted."
    else:
        return "Inverse is only defined for square matrices."

def sort_by_row(matrix):
    return np.sort(matrix, axis=1)

def sort_by_column(matrix):
    return np.sort(matrix, axis=0)

def sort_by_row_average(matrix):
    row_indices = np.argsort(np.mean(matrix, axis=1))
    return matrix[row_indices]

def change_matrix_element(matrix, row, col, new_value):
    if 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]:
        matrix[row, col] = new_value
        return matrix
    else:
        return "Invalid row or column index."

# Example usage
N, M = 4, 4  # Define matrix size
matrix = create_random_matrix(N, M)
print("Original Matrix:")
print(matrix)

print("\nDeterminant:")
print(calculate_determinant(matrix))

print("\nInverse:")
print(find_inverse(matrix))

print("\nSorted by row:")
print(sort_by_row(matrix))

print("\nSorted by column:")
print(sort_by_column(matrix))

print("\nSorted by row average:")
print(sort_by_row_average(matrix))

# Changing an element example
row, col, new_value = 2, 3, 50  # Example new value
matrix = change_matrix_element(matrix, row, col, new_value)
print("\nMatrix after modification:")
print(matrix)
def change_matrix_element(matrix, row, col, new_value):
    if 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]:
        matrix[row, col] = new_value
        return matrix
    else:
        return "Invalid row or column index."

def increase_column_by_2(matrix, col):
    if 0 <= col < matrix.shape[1]:
        matrix[:, col] += 2
        return matrix
    else:
        return "Invalid column index."

def add_vector_to_rows(matrix, vector):
    if len(vector) == matrix.shape[1]:
        return matrix + vector
    else:
        return "Vector length must match the number of columns in the matrix."

def calculate_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def calculate_svd(matrix):
    U, S, V = np.linalg.svd(matrix)
    return U, S, V

# Example usage
N, M = 4, 4  # Define matrix size
matrix = create_random_matrix(N, M)
print("Original Matrix:")
print(matrix)

print("\nDeterminant:")
print(calculate_determinant(matrix))

print("\nInverse:")
print(find_inverse(matrix))

print("\nSorted by row:")
print(sort_by_row(matrix))

print("\nSorted by column:")
print(sort_by_column(matrix))

print("\nSorted by row average:")
print(sort_by_row_average(matrix))

# Changing an element example
row, col, new_value = 2, 3, 50  # Example new value
matrix = change_matrix_element(matrix, row, col, new_value)
print("\nMatrix after modification:")
print(matrix)

# Increase column value example
col = 1  # Example column index
matrix = increase_column_by_2(matrix, col)
print("\nMatrix after increasing column values:")
print(matrix)

# Add vector to each row
vector = np.random.randint(-10, 10, M)
matrix = add_vector_to_rows(matrix, vector)
print("\nMatrix after adding vector to each row:")
print(matrix)

# Calculate rank
print("\nRank of matrix:")
print(calculate_rank(matrix))

# Calculate SVD
U, S, V = calculate_svd(matrix)
print("\nSVD Decomposition:")
print("U:")
print(U)
print("Singular values:")
print(S)
print("V:")
print(V)
