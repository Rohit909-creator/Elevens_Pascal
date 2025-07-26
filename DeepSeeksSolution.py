def generate_pascal_triangle(n_rows):
    if n_rows <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n_rows):
        prev = triangle[-1]
        left = prev + [0]
        right = [0] + prev
        new_row = [l + r for l, r in zip(left, right)]
        triangle.append(new_row)
    return triangle

# Example usage:
if __name__ == "__main__":
    n = 5
    triangle = generate_pascal_triangle(n)
    for row in triangle:
        print(row)