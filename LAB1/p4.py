def matrix_mul(matrix, rows, m):
    # Initialize result as an identity matrix for proper matrix multiplication
    result = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    
    # Perform matrix multiplication m times
    for _ in range(m):
        mul = [[0 for _ in range(rows)] for _ in range(rows)]
        for i in range(rows):
            for j in range(rows):
                for k in range(rows):
                    mul[i][j] += result[i][k] * matrix[k][j]
        result = mul
    
    # Print the result
    for row in result:
        print(row)

# main
# dimensions of the square matrix
rows = int(input("Enter the dimensions of the square matrix: "))
matrix = []
matrix1 = []
# matrix elements
print("Enter the elements of the matrix row by row:")
for i in range(rows):
    a = []
    for j in range(rows):
        a.append(int(input(f"Element [{i+1}][{j+1}]: ")))
    matrix.append(a)
m = int(input("Enter the argument: ")) #no. of times to be multiplied
matrix_mul(matrix, rows, m)