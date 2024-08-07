# Function to transpose a matrix
def transpose_matrix(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty matrix for the transposed result with switched dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Fill in the transposed matrix by swapping rows with columns
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Example matrix to transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the original matrix
print("Original matrix:")
for row in matrix:
    print(row)

# Transposing the matrix
transposed_matrix = transpose_matrix(matrix)

# Printing the transposed matrix
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
