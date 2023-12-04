def generate_pascals_triangle(numRows):
    # Check if numRows is 0, return an empty list
    if numRows == 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    # Iterate to generate subsequent rows in Pascal's Triangle
    for i in range(1, numRows):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Calculate each element as the sum of the two numbers above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)  # Append the current row to the triangle

    return triangle  # Return the generated Pascal's Triangle

numRows = int(input())  # Take user input for the number of rows
result = generate_pascals_triangle(numRows)  # Generate Pascal's Triangle
print(result)  # Print the result
